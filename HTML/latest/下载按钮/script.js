$('.upload').on('click touch', function(e) {

    e.preventDefault();

    var self = $(this);

    self.addClass('loading');
    setTimeout(function() {
        self.removeClass('loading');
    }, 4200)

});