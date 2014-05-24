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
    }
  });

  grunt.loadNpmTasks('grunt-contrib-requirejs');

  grunt.registerTask('default', ['requirejs']);

};