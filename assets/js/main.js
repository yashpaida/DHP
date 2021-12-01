var stepper1

var stepperForm

document.addEventListener('DOMContentLoaded', function() {
    stepper1 = new Stepper(document.querySelector('#stepper1'))

    var btnNextList = [].slice.call(document.querySelectorAll('.btn-next-form'))


    btnNextList.forEach(function(btn) {
        btn.addEventListener('click', function() {
            stepperForm.next()
        })
    })
})