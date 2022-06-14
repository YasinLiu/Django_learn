let randomNumer = Math.floor(Math.random() * 100) + 1;

const guesses = document.querySelector('.guesses');
const lastResult = document.querySelector('.lastResult');
const lowOrHi = document.querySelector('.lowOrHi');

const guessSubmit = document.querySelector('.guessSubmit');
const guessField = document.querySelector('.guessField');

let guessCount = 1;
let resetButton;

function checkGuess() {
    let userGuess = Number(guessField.value);
    if (guessCount === 1) {
        guesses.textContent = '上次猜的数：';
    }
    guesses.textContent += userGuess + ' ';

    if (userGuess === randomNumer) {
        lastResult.textContent = '恭喜你！猜对了';
        lastResult.style.backgroundColor = 'green';
        lowOrHi.textContent = '';
        setGameOver();
    }
    else if (guessCount === 10) {
        lastResult.textContent = '!!!GAME OVER!!!';
        setGameOver();
    }
    else {
        lastResult.textContent = '你猜错了!';
        lastResult.style.backgroundColor = 'red';
        if (userGuess < randomNumer) {
            lowOrHi.textContent = '你猜低了！';
        }
        else {
            lowOrHi.textContent = '你猜高了！';
        }
    }

    guessCount ++;
    guessField.value = '';
    guessField.focus();
}

guessSubmit.addEventListener('click', checkGuess);

function setGameOver() {
    guessField.disabled = true;
    guessSubmit.disabled = true;
    resetButton = document.createElement('button');
    resetButton.textContent = '开始新游戏';
    document.body.appendChild(resetButton);
    resetButton.addEventListener('click', resetGame);
}

function resetGame() {
    guessCount = 1;

    const resetPara = document.querySelectorAll('.resultParas p');
    for (let i=0; i<resetPara.length; i++) {
        resetPara[i].textContent = '';
    }

    resetButton.parentNode.removeChild(resetButton);

    guessField.disabled = false;
    guessSubmit.disabled = false;
    guessField.value = '';
    guessField.focus();

    lastResult.style.backgroundColor = 'white';

    randomNumer = Math.floor(Math.random() * 100) + 1;
}

