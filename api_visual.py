#Flask 앱
from flask import Flask, render_template, request, Blueprint, Markup

#dataframe 다루기
import numpy as np
import pandas as pd

#시각화 그래프 저장
import base64
from io import BytesIO

#시각화
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib.figure import Figure
import seaborn as sns
from bokeh.plotting import figure
from bokeh import *
from bokeh.embed import components

app = Flask(__name__)
visual = Blueprint('visual', __name__)

#가공된 18~19, 20~21년도 csv파일 ('trending_date','title','channel_title','category_id','publish_time','tags','views','likes','dislikes','comment_count','trending_ym')
kr18 = pd.read_csv('static/csv_file/kr18_ver2.csv')
kr20 = pd.read_csv('static/csv_file/kr20_ver2.csv')
corona_info = pd.read_csv('static/csv_file/corona_cases_ver2.csv')
crosstab = pd.read_csv('static/csv_file/crosstab.csv')

#기본 데이터 : 영상 데이터 있는것(list)  / 카테고리는 존재하지만 trending 영상은 없는 것(list2)
category_list = {'1' : 'Film & Animation', '2' : 'Autos & Vehicles', '10' : 'Music', '15' : 'Pets & Animals', '17' : 'Sports','19' : 'Travel & Events',
                '20' : 'Gaming', '22' : 'People & Blogs','23' : 'Comedy','24' : 'Entertainment', '25' : 'News & Politics',
                '26' : 'Howto & Style', '27' : 'Education','28' : 'Science & Technology','29' : 'Nonprofits & Activism'}

category_list2 = {'18' : 'Short Movies', '21' : 'Videoblogging', '30' : 'Movies', '31' : 'Anime/Animation', '32' : 'Action/Adventure',
                '33' : 'Classics','34' : 'Comedy', '35' : 'Documentary', '36' : 'Drama','37' : 'Family', '38' : 'Foreign','39' : 'Horror',
                '40' : 'Sci-Fi/Fantasy', '41' : 'Thriller', '42' : 'Shorts', '43' : 'Shows', '44' : 'Trailers'}
corr = {'Travel & Events': 0.758423, 'People & Blogs':0.724855, 'Howto & Style':0.606430, 'Gaming':0.240503, 'Entertainment':0.167289, 'Science & Technology':0.112975, 'Nonprofits & Activism':0.031593, 'Music':-0.095519, 'Sports':-0.144160, 'Autos & Vehicles':-0.182005, 'Pets & Animals':-0.208127, 'Comedy':-0.219434, 'News & Politics':-0.408071, 'Film & Animation':-0.482346, 'Education':-0.649733}



#홈페이지 "/"
@visual.route('/visual', methods = ['GET'])
def home():
    return render_template('visual_home.html')

#기능1 : 카테고리 별 영상 수 변화
@visual.route('/vid-cnt', methods = ['GET', 'POST'])
def vidcnt():
    if request.method == 'POST':
        try:
            category_id = request.form['category_id']
            category_id_name = category_list[category_id]
        except:
            msg = "정확한 값을 입력하세요"
            return render_template('visual_video_count_home.html', category_list = category_list, msg=msg)
        category_id = request.form['category_id']
        category_id_name = category_list[category_id]

        user_want_18 = kr18[kr18['category_id']==int(category_id)]
        user_want_20 = kr20[kr20['category_id']==int(category_id)]
        trending_ym_18 = user_want_18['trending_ym']
        trending_ym_20 = user_want_20['trending_ym']
        count_18 = pd.Series(trending_ym_18.value_counts())
        count_20 = pd.Series(trending_ym_20.value_counts())
        v_cnt_18 = pd.DataFrame({"count" : count_18})
        v_cnt_20 = pd.DataFrame({"count" : count_20})
        v_cnt_18 = v_cnt_18.sort_index(ascending=True)
        v_cnt_20 = v_cnt_20.sort_index(ascending=True)
        change_vd_cnt=int(count_20.mean()-count_18.mean())
        if change_vd_cnt >= 0:
            expr_word = "증가"
        else:
            expr_word = "감소"
            change_vd_cnt *= -1
        color_list = ["#bae4bc", "#43a2ca", "#c994c7", "#a8ddb5", "#fc8d59", "#7bccc4", "#fdcc8a"]
        fig, ax = plt.subplots()
        plt.bar(v_cnt_18.index, v_cnt_18['count'], color=color_list[int(category_id)%7], width=0.4, label='count')  #색깔은 category_id에 달라지게끔
        plt.bar(v_cnt_20.index, v_cnt_20['count'], color=color_list[int(category_id)%7-1], width=0.4, label='count')  #색깔은 category_id에 달라지게끔
        plt.xticks(rotation = 60)

        buf = BytesIO()
        plt.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        plt.close(fig)
        return render_template('visual_video_count_result.html', category_id_name = category_id_name, data=data, expr_word=expr_word, change_vd_cnt=change_vd_cnt)
    else:
        return render_template('visual_video_count_home.html', category_list = category_list)

#기능2: 평균 조회수 비교
@visual.route('/comp-mean-views', methods = ['GET', 'POST'])
def compare_mean_views():
    if request.method == 'POST':
        try:
            category_id = request.form.get('category_id')
            category_id_name = category_list[category_id]
        except:
            msg = "정확한 값을 입력하세요"
            return render_template('visual_compare_mean_views_home.html', category_list = category_list, msg=msg)
        user_want_18 = kr18[kr18['category_id']==int(category_id)]
        user_want_20 = kr20[kr20['category_id']==int(category_id)]
        user_want_18 = user_want_18.drop(columns=['trending_date', 'title', 'channel_title', 'category_id', 'publish_time', 'tags', 'likes', 'dislikes', 'comment_count'])
        user_want_20 = user_want_20.drop(columns=['trending_date', 'title', 'channel_title', 'category_id', 'publish_time', 'tags', 'likes', 'dislikes', 'comment_count'])
        user_want_18.drop(user_want_18[user_want_18['views']==0].index, inplace=True)
        user_want_20.drop(user_want_20[user_want_20['views']==0].index, inplace=True)
        mean_views_18 = user_want_18.groupby('trending_ym').mean()
        mean_views_20 = user_want_20.groupby('trending_ym').mean()
        bef_covid = mean_views_18.mean(axis=0)
        aft_covid = mean_views_20.mean(axis=0)
        vari = '%3.2f' % (aft_covid/bef_covid)

        plt.ticklabel_format(style='plain')
        plt.plot(mean_views_18)
        plt.plot(mean_views_20)
        plt.xticks(rotation=60)

        buf = BytesIO()
        plt.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        plt.close()
        return render_template('visual_compare_mean_views_result.html', category_id_name=category_id_name, data=data, vari=vari)
    else:
        return render_template('visual_compare_mean_views_home.html', category_list = category_list)

# 기능3: 코로나 전후 영상들의 카테고리 순위 및 비율 변화
@visual.route('/ratio-ch-vid', methods = ['GET', 'POST'])
def ratio_ch_vid():
    if request.method == 'POST':
        try:
            label_num = request.form['label_num']
            assert(0< int(label_num) < 15)
            label_num = int(label_num)
        except:
            msg = "정확한 값을 입력하세요"
            return render_template('visual_ratio_change_video_home.html', category_list = category_list, msg=msg)

        #데이터가공(views컬럼 필요없지만 나중에 views로 통계낼 수도 있을 경우 확장성 고려)
        ver1_kr18 = kr18.iloc[:,[3,6]]
        ver1_kr20 = kr20.iloc[:,[3,6]]
        ver2_kr18 = ver1_kr18['category_id'].value_counts()
        ver2_kr20 = ver1_kr20['category_id'].value_counts()
        pd_kr18 = pd.DataFrame({'category_id':ver2_kr18.index, 'video_cnt':ver2_kr18.values})
        pd_kr20 = pd.DataFrame({'category_id':ver2_kr20.index, 'video_cnt':ver2_kr20.values})
        del_row1 = pd_kr18[(pd_kr18['category_id']==43)|(pd_kr18['category_id']==44)].index
        del_row2 = pd_kr20[(pd_kr20['category_id']==43)|(pd_kr20['category_id']==44)].index
        pd_kr18.drop(del_row1, inplace=True)
        pd_kr20.drop(del_row2, inplace=True)
        pd_kr18['category_name'] = pd_kr18['category_id'].apply(lambda x: category_list[str(x)])
        pd_kr20['category_name'] = pd_kr20['category_id'].apply(lambda x: category_list[str(x)])
        labels_18 = list(pd_kr18['category_name'])
        vals_18 = list(pd_kr18['video_cnt'])
        labels_20 = list(pd_kr20['category_name'])
        vals_20 = list(pd_kr20['video_cnt'])

        rank_change = []
        for i in range(label_num):
            a = i-labels_18.index(labels_20[i])
            if a > 0:
                result = f"{a}순위 하강"
            elif a < 0:
                result = f"{-a}순위 상승"
            else:
                result = "변동 없음"
            rank_change.append(result)
        explode_list=[]
        for i in range(label_num):
            explode_list.append(float(i*0.015))

        top5_labels_18 = labels_18[:label_num]
        top5_vals_18 = vals_18[:label_num]
        top5_labels_20 = labels_20[:label_num]
        top5_vals_20 = vals_20[:label_num]

        colors =  ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff', '#E3CEF6'
            ,'#bae4bc', '#43a2ca', '#c994c7', '#a8ddb5', '#fc8d59', '#7bccc4', '#fdcc8a']
        plt.figure(figsize=(10,4))  #13,5
        plt.subplot(121)
        plt.pie(top5_vals_18, labels=top5_labels_18, radius=0.9, autopct='%0.1f%%', startangle=-20, colors=colors, explode=explode_list)
        plt.title('Before corona \n(2017-2018)')
        plt.axis('equal')
        plt.subplot(122)
        plt.pie(top5_vals_20, labels=top5_labels_20, autopct='%0.1f%%', startangle=-20, colors=colors, explode=explode_list)
        plt.title('After corona \n(2020-2021)')
        plt.axis('equal')
        
        buf = BytesIO()
        plt.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        plt.close()
        return render_template('visual_ratio_change_video_result.html', data=data, label_num=label_num, rank_change=rank_change, category_name=labels_20)
    else:
        return render_template('visual_ratio_change_video_home.html', category_list = category_list)

#기능 4: 멀티 분석(전체카테고리 or 개별카테고리 선택가능)
@visual.route('/multi-analysis', methods = ['GET', 'POST'])
def multi_analysis():
    youtube_col_list = ['views', 'likes', 'dislikes', 'comment_count', 'likes_ratio']
    corona_col_list = ['local_outbreak', 'imported_cases', 'death', 'total_death', 'new_cases', 'total_cases', 'variation']
    color_list = ['darkorange','g', 'b','r']
    new_category_list={'0':'All Categories'}
    new_category_list.update(category_list)
    if request.method == 'POST':
        try:
            selection_1_num = request.form['selection_1_num']
            assert(0< int(selection_1_num) < 8)
            selection_1_num = int(selection_1_num)
            selection_2_num = request.form['selection_2_num']
            assert(0< int(selection_2_num) < 6)
            selection_2_num = int(selection_2_num)
            category_id = request.form['category_id']
            category_id_name = new_category_list[category_id]
        except:
            msg = "정확한 값을 입력하세요"
            return render_template('visual_multi_analysis_home.html', enumerate=enumerate, youtube_col_list=youtube_col_list, corona_col_list=corona_col_list, msg=msg, category_list=new_category_list)
        if int(category_id) == 0:
            #전체 카테고리인 경우
            kr20.replace(0, np.nan)
            kr20_2 = kr20.groupby(['trending_date'], as_index=False).mean()
            def likes_per_dislikes(row):
                return row['likes']/(row['likes']+row['dislikes']+1)*100
            kr20_2['likes_ratio']=kr20_2.apply(lambda row: likes_per_dislikes(row), axis=1)
            kr20_2['trending_date']=pd.to_datetime(kr20_2['trending_date'], format='%Y-%m-%d')
            corona_info['date']=pd.to_datetime(corona_info['date'], format='%Y-%m-%d')

            fig, ax1 = plt.subplots(figsize=(13,6))
            ax2=ax1.twinx()
            selection_1 = corona_col_list[selection_1_num-1]
            selection_2 = youtube_col_list[selection_2_num-1]
            sns.lineplot(x='date', y=f"{selection_1}", data=corona_info, ax=ax1, color=color_list[selection_2_num%2], label=f"{selection_1}")
            sns.lineplot(x='trending_date', y=f'{selection_2}', data=kr20_2 , ax=ax2, color=color_list[selection_2_num%2+2], label=f"{selection_2}")
            ax1.legend(loc=2)
            ax2.legend(loc=1)
            ax1.set_xlabel(None)
            ax1.set_ylabel(f"{selection_1}", size=15)
            ax2.set_ylabel(f'{selection_2}', size=15)
            ax1.set_title(f"{selection_1} & {selection_2}")
            #scientific notation제거
            plt.ticklabel_format(style='plain', axis='y',useOffset=False)
            buf = BytesIO()
            plt.savefig(buf, format='png')
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            plt.close(fig)
            return render_template('visual_multi_analysis_result.html', data=data, selection_1=selection_1, selection_2=selection_2)
        else:
            #개별 카테고리를 선택할 경우
            #먼저 카테고리로 추출
            category_filter = kr20[kr20['category_id']==int(category_id)]
            category_filter.replace(0, np.nan)
            kr20_2 = category_filter.groupby(['trending_date'], as_index=False).mean()
            def likes_per_dislikes(row):
                result = row['likes']/(row['likes']+row['dislikes']+1)*100
                if result < 5:
                    result = 95
                return result
            kr20_2['likes_ratio']=kr20_2.apply(lambda row: likes_per_dislikes(row), axis=1)
            kr20_2['trending_date']=pd.to_datetime(kr20_2['trending_date'], format='%Y-%m-%d')
            corona_info['date']=pd.to_datetime(corona_info['date'], format='%Y-%m-%d')
            fig, ax1 = plt.subplots(figsize=(13,6))
            ax2=ax1.twinx()
            selection_1 = corona_col_list[selection_1_num-1]
            selection_2 = youtube_col_list[selection_2_num-1]
            sns.lineplot(x='date', y=f"{selection_1}", data=corona_info, ax=ax1, color=color_list[selection_2_num%2], label=f"{selection_1}")
            sns.lineplot(x='trending_date', y=f'{selection_2}', data=kr20_2 , ax=ax2, color=color_list[selection_2_num%2+2], label=f"{selection_2}")
            plt.ticklabel_format(style='plain', axis='y',useOffset=False)
            ax1.legend(loc=2)
            ax2.legend(loc=1)
            ax1.set_xlabel(None)
            ax1.set_ylabel(f"{selection_1}", size=15)
            ax2.set_ylabel(f'{selection_2}', size=15)
            ax1.set_title(f"{selection_1} & {selection_2}")
            buf = BytesIO()
            plt.savefig(buf, format='png')
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            plt.close(fig)
            return render_template('visual_multi_analysis_category_based_result.html', data=data, selection_1=selection_1, selection_2=selection_2, category_id_name=category_id_name)
    else:
        return render_template('visual_multi_analysis_home.html', enumerate=enumerate, youtube_col_list=youtube_col_list, corona_col_list=corona_col_list, category_list=new_category_list)

#기능 5: 코로나 관련 영상 추출후 멀티분석기능 제공(전체데이터에서 2%밖에 안되는 적은 데이터량이라 개별 카테고리 기능은 의미가없어 전체카테고리 데이터만 제공)
@visual.route('/corona-related-multi-analysis', methods = ['GET', 'POST'])
def corona_related_multi_analysis():
    youtube_col_list = ['views', 'likes', 'dislikes', 'comment_count', 'likes_ratio']
    corona_col_list = ['local_outbreak', 'imported_cases', 'death', 'total_death', 'new_cases', 'total_cases', 'variation']
    color_list = ['darkorange','g', 'b','r']
    corona_related_word =['코로나', '바이러스','변이', '백신', '거리두기', '코비드', 'corona', 
                    'covid', '확진자', '사망자', '위드', '확진','마스크','전파자','방역', '자가격리', '비대면']
    corona_not_related_word =['drama', '뮤직비디오']
    expr01 = kr20['title'].str.lower().str.contains('|'.join(corona_related_word), na=False)
    expr02 = kr20['tags'].str.lower().str.contains('|'.join(corona_related_word), na=False)
    expr03 = kr20['title'].str.lower().str.contains('|'.join(corona_not_related_word), na=False)
    expr04 = kr20['tags'].str.lower().str.contains('|'.join(corona_not_related_word), na=False)
    corona_related_filter = ((expr01)|(expr02))&~((expr03)|(expr04))

    if request.method == 'POST':
        try:
            selection_1_num = request.form['selection_1_num']
            assert(0< int(selection_1_num) < 8)
            selection_1_num = int(selection_1_num)
            selection_2_num = request.form['selection_2_num']
            assert(0< int(selection_2_num) < 6)
            selection_2_num = int(selection_2_num)
        except:
            msg = "정확한 값을 입력하세요"
            return render_template('visual_corona_related_multi_analysis_home.html', enumerate=enumerate, youtube_col_list=youtube_col_list, category_list=category_list, corona_col_list=corona_col_list, msg=msg)
        kr20_1=kr20[corona_related_filter]
        kr20_1.replace(0, np.nan)

        kr20_2 = kr20_1.groupby(['trending_date'], as_index=False).mean()
        def likes_per_dislikes(row):
            result = row['likes']/(row['likes']+row['dislikes']+1)*100
            if result < 5:
                result = 95
            return result
        kr20_2['likes_ratio']=kr20_2.apply(lambda row: likes_per_dislikes(row), axis=1)
        kr20_2['trending_date']=pd.to_datetime(kr20_2['trending_date'], format='%Y-%m-%d')
        corona_info['date']=pd.to_datetime(corona_info['date'], format='%Y-%m-%d')

        fig, ax1 = plt.subplots(figsize=(13,6))
        ax2=ax1.twinx()
        selection_1 = corona_col_list[selection_1_num-1]
        selection_2 = youtube_col_list[selection_2_num-1]
        sns.lineplot(x='date', y=f"{selection_1}", data=corona_info, ax=ax1, color=color_list[selection_2_num%2], label=f"{selection_1}")
        sns.lineplot(x='trending_date', y=f'{selection_2}', data=kr20_2 , ax=ax2, color=color_list[selection_2_num%2+2], label=f"{selection_2}")
        plt.ticklabel_format(style='plain', axis='y',useOffset=False)
        ax1.legend(loc=2)
        ax2.legend(loc=1)
        ax1.set_xlabel(None)
        ax1.set_ylabel(f"{selection_1}", size=15)
        ax2.set_ylabel(f'{selection_2}', size=15)
        ax1.set_title(f"{selection_1} & {selection_2}")
        
        buf = BytesIO()
        plt.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        plt.close(fig)
        return render_template('visual_corona_related_multi_analysis_result.html', data=data, selection_1=selection_1, selection_2=selection_2)
    else:
        return render_template('visual_corona_related_multi_analysis_home.html', enumerate=enumerate, youtube_col_list=youtube_col_list, corona_col_list=corona_col_list, category_list=category_list)


#기능 6: Bokeh 상관관계 그래프
@visual.route('/correlation-bokeh', methods=['GET', 'POST'])
def corona_category():
    if request.method == 'POST':
        try:
            category_id = request.form['category_id']
            category_id_name = category_list[category_id]
        except:
            msg = "정확한 값을 입력하세요"
            return render_template('visual_correlation_bokeh_home.html', category_list = category_list, msg=msg)
        category_id = request.form['category_id']
        category_id_name = category_list[category_id]

        x = crosstab['confirmed'].tolist()
        y = crosstab[category_id_name].tolist()
        p = figure(plot_width=500, plot_height=400, title=category_id_name, x_axis_label='Confirmed', y_axis_label=category_id_name)
        p.circle(x, y, line_color='#fdae61', fill_color='#fdae61', alpha=0.6, size=10)
        p.title.text_font_size = '15px'

        script, div = components(p)
        script = Markup(script)
        div = Markup(div)

        return render_template('visual_correlation_bokeh_result.html', category_id_name=category_id_name, corr=corr[category_id_name], script=script, div=div)
    else:
        return render_template('visual_correlation_bokeh_home.html', category_list = category_list)

#기능 7: 감정분석 기능. 이건 이미 결과가 나와있는 것이고, 데이터 처리하는데 오랜시간이 걸리므로 이미지를 바로 띄워줌
@visual.route('/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        user_want = request.form['sentiment_data']
        print(user_want)
        return render_template('visual_sentiment_analysis_result.html', user_want=user_want)
    else:
        return render_template('visual_sentiment_analysis_home.html')
