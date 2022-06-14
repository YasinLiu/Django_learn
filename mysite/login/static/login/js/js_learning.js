function createParagraph() {
    let para = document.createElement('p');
    para.textContent = '老六，你点了这个按钮！';
    document.body.appendChild(para);
}

const buttons = document.querySelectorAll('button');

for(let i=0; i<buttons.length; i++) {
buttons[i].addEventListener('click', createParagraph);
}
