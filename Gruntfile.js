module.exports = function (grunt) {

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
    }
  });

  grunt.loadNpmTasks('grunt-sass');

  grunt.registerTask('default', ['sass']);

};