$(document).ready(function () {


    $("#detail-payement").show();
    $("#cacher-detail").hide();
    $("#cadre-ajouts").hide();


    $("#ajouter").click(function () {

        $("#cadre-ajouts").show();
        $("#ajouter").hide();

        $('html').css({
            'overflow': 'hidden', 'height': '100%'

        });


    });


    $("#afficher-detail").click(function () {

        $("#detail-payement").show();
        $("#afficher-detail").hide();
        $("#cacher-detail").show();


    });


    $("#cacher-detail").click(function () {

        $("#detail-payement").hide();
        $("#afficher-detail").show();
        $("#cacher-detail").hide();


    });

    $(".close").click(function () {

        $("#cadre-message").hide();


    });


});


function printDiv(divName) {
    var printContents = document.getElementById('badge').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


function printDiv2(divName) {
    var printContents = document.getElementById('cadre-recu').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


function printDiv3(divName) {
    var printContents = document.getElementById('imprimer-classe').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


function printDiv4(divName) {
    var printContents = document.getElementById('badge').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


function printDiv5(divName) {
    var printContents = document.getElementById('imprimer-salaire').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


function printDiv6(divName) {
    var printContents = document.getElementById('recu-salaire').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


function printDiv7(divName) {
    var printContents = document.getElementById('imprimer-salaire').innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}














