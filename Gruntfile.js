module.exports = function (grunt) {

  grunt.initConfig({
    requirejs: {
      compile: {
        options: {
          baseUrl: 'js',
          mainConfigFile: "js/init.js",
          name: "main", // assumes a production build using almond
          out: "js/main.build.js",
          optimize: 'uglify2'
        }
      }
    },
    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'css/app.css': 'scss/app.scss'
        }        
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-requirejs');
  grunt.loadNpmTasks('grunt-sass');

  grunt.registerTask('default', ['sass']);

};