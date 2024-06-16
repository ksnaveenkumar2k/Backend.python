const characters = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c",
"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
"u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6", "7", "8",
"9","~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=",
"{","[","}","]",",","|",":",";","<",">",".","?","/"];

const firstRectEl = document.getElementById('rectangle-text')
const secondRectEl = document.getElementById('rectangle-text-1')
const passwordBtn = document.querySelector('.password-generate')
const copyFirstBtn = document.getElementById('copy-btn')
const copySecondBtn = document.getElementById('copy-btn-1')

passwordBtn.addEventListener('click',()=>{
    firstRectEl.innerHTML = ''
    secondRectEl.innerHTML = ''

    for (let i=0; i<14; i++){
        let randomFirstNumber = Math.floor(Math.random()*characters.length)
        let randomSecondNumber = Math.floor(Math.random()*characters.length)
        firstRectEl.innerHTML += characters[randomFirstNumber]
        secondRectEl.innerHTML += characters[randomSecondNumber]
    }
    copyFirstBtn.style.display = 'block'
    copySecondBtn.style.display = 'block'
    copiedAlert(copyFirstBtn)
    copiedAlert(copySecondBtn)
})

function copiedAlert(data){
    data.addEventListener('click',()=>{
        if (data === copyFirstBtn){
            navigator.clipboard.writeText(firstRectEl.textContent)
        }
        else if (data === copySecondBtn){
            navigator.clipboard.writeText(secondRectEl.textContent)
        }
        alert("Copied to clipboard")
    })
}