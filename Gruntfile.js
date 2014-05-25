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
      dist: {
        files: {
          'styles/main.css': 'styles/main.scss'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-requirejs');
  grunt.loadNpmTasks('grunt-contrib-sass');

  grunt.registerTask('default', ['sass']);

};