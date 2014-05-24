define([
    'marionette',
    'backbone'
], function(Marionette) {
    'use strict';

    var App = new Marionette.Application();

    Backbone.history.start({
        pushState: true,
        hashChange: false
    });

    return App;
});
