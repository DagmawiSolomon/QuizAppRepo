document.querySelectorAll('.choices_btn').forEach(item => {
    item.addEventListener('click', event => {
        if (item.id == "correct"){
            item.style.backgroundColor =" #d4edda"
            item.style.color = "#155724"
            item.style.border = "1px solid #c3e6cb"
        }
        else if(item.id="wrong"){
            item.style.backgroundColor =" #f8d7da"
            item.style.color = "#721c24"
            item.style.border = " 1px solid #f5c6cb"
        }
})
})