const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')
const QuizContainer = document.getElementById('scoreboard')
const ScoreBoardButton = document.getElementById('score')
const TlacidloHodnotenia = document.getElementById('hodnotenie')

var correctAnswers = 0



let shuffledQuestions, currentQuestionIndex





startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', () => {
    currentQuestionIndex++
    setNextQuestion()
})

function startGame() {
    startButton.classList.add('hide')
    shuffledQuestions = questions.sort(() => Math.random() - .5)
    currentQuestionIndex = 0
    questionContainerElement.classList.remove('hide')
   
    setNextQuestion()
}

function setNextQuestion() {
    resetState()
    showQuestion(shuffledQuestions[currentQuestionIndex])
}

    
    
function showQuestion(question) {
    questionElement.innerText = question.question
    question.answers.forEach(answer => {
        const button = document.createElement('button')
        button.innerText = answer.text
        button.classList.add('btn')
        if (answer.correct) {
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click', selectAnswer)
        answerButtonsElement.appendChild(button)
    })
}

function resetState() {
    clearStatusClass(document.body)
    nextButton.classList.add('hide')
    while (answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild)
    }
}

function selectAnswer(e) {

    const selectedButton = e.target
    const correct = selectedButton.dataset.correct
    if (correct) {
        correctAnswers++
    }
    setStatusClass(document.body, correct)
    Array.from(answerButtonsElement.children).forEach(button => {
        setStatusClass(button, button.dataset.correct)
    })
    if (shuffledQuestions.length > currentQuestionIndex + 1) {
        nextButton.classList.remove('hide')
    } else {
        TlacidloHodnotenia.classList.remove('hide')
    }




}
function Hodnotenie() {
    
    ScoreBoardButton.innerText = correctAnswers.toString() + "/" + shuffledQuestions.length.toString()
    correctAnswers = 0

    QuizContainer.classList.remove('hide')
    ScoreBoardButton.classList.remove('hide')
    questionContainerElement.classList.add('hide')
    questionElement.classList.add('hide')
    TlacidloHodnotenia.classList.add('hide')
}
function setStatusClass(element, correct) {
    clearStatusClass(element)
    if (correct) {
        element.classList.add('correct')
    } else {
        element.classList.add('wrong')
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct')
    element.classList.remove('wrong')
}

const questions = [
    {
        question: 'Kedy bude môcť byť vyradený spis, ktorý bol uzatvorený v roku 2014 a má lehotu uloženia 5 rokov?',
        answers: [
            { text: 'a) 2019', correct: false },
            { text: 'b) 2020', correct: true },
            { text: 'c) 2021', correct: false }
        ]
    },
    {
        question: 'Čo robí pracovník podateľne?',
        answers: [
            {
                text: 'a) Eviduje doručený záznam', correct: true },
            { text: 'b) Vytvára spis', correct: false },
            { text: 'c) Realizuje vyraďovacie konanie', correct: false }
           
        ]
    },
    {
        question: 'Akú má farbu nápisová pečiatka?',
        answers: [
            { text: 'a) Červenú', correct: true },
            { text: 'b) Modrú', correct: false },
            { text: 'c) Čiernu', correct: false }
            
        ]
    },
    {
        question: 'Ktoré označenie patrí číslu spisu?',
        answers: [
            { text: 'a) 12345/2022', correct: false },
            { text: 'b) 56789/2019/ORTT', correct: true },
            { text: 'c) 56789/2019/ORTT-3', correct: false }

        ]
    },
    {
        question: 'Kto vykonáva odborný dozor za oblasť registratúry na ŽSR?',
        answers: [
            {
                text: 'a) Ministerstvo financií SR', correct: false
            },
            { text: 'b) Ministerstvo vnútra SR', correct: true },
            { text: 'c) Ministerstvo dopravy SR', correct: false }

        ]
    }
]