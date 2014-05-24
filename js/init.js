require.config({
    deps: ['main'],

    shim: {
        angular: {
            exports: 'angular'
        },
        underscore: {
            exports: '_'
        }
    },

    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        underscore: '../bower_components/underscore/underscore',
        angular: '../bower_components/angular/angular'
    }
});