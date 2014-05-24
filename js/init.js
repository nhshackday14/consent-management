require.config({
    deps: ['main'],

    shim: {
        angular: {
            exports: 'angular'
        },
        underscore: {
            exports: '_'
        },
        backbone: {
            deps: ['jquery', 'underscore'],
            exports: 'Backbone'
        },
        marionette: {
            exports: 'Backbone.Marionette',
            deps: ['backbone']
        }
    },

    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        underscore: '../bower_components/underscore/underscore',
        backbone: '../bower_components/backbone/backbone',
        marionette: '../bower_components/marionette/lib/backbone.marionette',
        'backbone.wreqr': '../bower_components/backbone.wreqr/lib/backbone.wreqr',
        angular: '../bower_components/angular/angular'
    }
});