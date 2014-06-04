module.exports = function (grunt) {
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-sass');

  grunt.initConfig({
    sass: {
      options: {
        includePaths: ['public/bower_components/foundation/scss']
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'public/css/app.css': 'public/scss/app.scss'
        }
      }
    },

    concat: {
        js : {
          src: [
                "public/bower_components/jquery/dist/jquery.min.js",
                "public/bower_components/typeahead.js/dist/typeahead.bundle.js",
                "public/bower_components/fastclick/lib/fastclick.js",
                "public/bower_components/foundation/js/foundation.min.js",
                "public/bower_components/modernizr/modernizr.js",
                "public/bower_components/angular/angular.min.js",
                "public/bower_components/angular-route/angular-route.min.js",
                "public/bower_components/angular-resource/angular-resource.min.js",
                "public/js/app.js",
                "public/js/services/consentSrv.js",
                "public/js/directives/consentDrv.js",
                "public/js/controllers/consentCtrl.js",
                "public/js/foundation.js",
          ],
          dest: 'public/js/main.js'
      }
    }
  });

  grunt.registerTask('default', ['concat', 'sass']);
  grunt.registerTask('concat_js', ['concat']);
  grunt.registerTask('compile_styles', ['sass']);

};
