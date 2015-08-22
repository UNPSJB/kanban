$(function(){
   $( ".column" ).sortable({
      connectWith: ".column",
      handle: ".tarjeta-header",
      cancel: ".tarjeta-toggle",
      start: function (event, ui) {
        ui.item.addClass('tilt');
      },
      stop: function (event, ui) {
        ui.item.removeClass('tilt');
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