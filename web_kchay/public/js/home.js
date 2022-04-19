/*------------------ HOME ----------------*/
/*контейнер новости*/
$(document).ready(function () {
    $(".my__courses").hide();
    $(".my__certificates").hide();
    $("#personal__information-btn").click(function () {
        $(".my__courses").hide();
        $(".my__certificates").hide();
        $(".personal__information").show();
    });

    $("#my__courses-btn").click(function () {
        $(".my__certificates").hide();
        $(".personal__information").hide();
        $(".my__courses").show();
    });

    $("#my__certificates-btn").click(function () {
        $(".personal__information").hide();
        $(".my__courses").hide();
        $(".my__certificates").show();
    });
});
/*--/контейнер новости*/


/*------------------ /HOME ----------------*/