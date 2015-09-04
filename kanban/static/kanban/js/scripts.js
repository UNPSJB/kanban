$(function(){
   $( ".column" ).sortable({
      connectWith: ".column",
      handle: ".tarjeta-header",
      cancel: ".tarjeta-toggle",
      start: function (event, ui) {
        $(".glyphicon-move", $(ui.item)).toggleClass('hide');
      },
      stop: function (event, ui) {
        $(".glyphicon-move", $(ui.item)).toggleClass('hide');
        var column = $(ui.item).closest(".column").data()["id"];
        var tarjeta = $(ui.item).data()["id"];
        $.get('/kanban/tarjeta/' + tarjeta + '/mover/' + column, function() {
            console.log("Movido");
        });
      }
    });
   $( ".ver-tarjeta" ).click(function(e){
        e.preventDefault();
        var id = $(e.currentTarget).data()["id"];
        var title = $(e.currentTarget).data()["title"];
        $('#tarjeta-modal .modal-title').html('<h4 class="modal-title">'+title+'</h4>')
        $('#tarjeta-modal .modal-body').load('/kanban/tarjeta/' + id + '/modal/', function(){
            $('#tarjeta-modal').modal();
        });
   });
});