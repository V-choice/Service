/*!
 * Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
 * Copyright 2013-2021 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project

let ticking = false;

function isElementUnderBottom(elem, triggerDiff) {
    const { top } = elem.getBoundingClientRect();
    const { innerHeight } = window;
    return top > innerHeight + (triggerDiff || 0);
}

function handleScroll() {
    ticking = false;

    const upOnScrollElems = document.querySelectorAll('.up-on-scroll');
    upOnScrollElems.forEach(elem => {
        if (isElementUnderBottom(elem)) {
            elem.style.opacity = "0";
            elem.style.transform = 'translateY(70px)';
        } else {
            elem.style.opacity = "1";
            elem.style.transform = 'translateY(0px)';
        }
    });

    const productImg = document.querySelector('.diff-desc-image-wrap .image-wrap');
    const productImgRect = productImg.getBoundingClientRect();
    if (productImgRect.top < 0) {
        productImg.style.transform = `translateY(${-1 * productImgRect.top * 0.8 }px)`
    } else {
        productImg.style.transform = 'none';
    }

    const changeBgSection = document.querySelector('.background-change-wrap');
    const changeBgImg = document.querySelector('.background-change-wrap > div');
    const { top: bgTop, height: bgHeight } = changeBgSection.getBoundingClientRect();
    if (bgTop < 0) {
        const rate = (-1) * bgTop / 4;
        changeBgImg.style.filter = `grayscale(${rate}%)`;
        changeBgImg.style.opacity = `${(100-rate/5) / 100}`;
    } else {
        changeBgImg.style.filter = 'none';
        changeBgImg.style.opacity = `1`;
    }
}

function requestTick() {
    if (!ticking) {
        requestAnimationFrame(handleScroll);
    }
    ticking = true;
}

window.addEventListener('scroll', requestTick);