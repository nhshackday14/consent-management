angular.module('consentApp', ['ngRoute'])

.config(function($routeProvider, $locationProvider) {
  $routeProvider
   .when('/search', {
    templateUrl: 'templates/searchResults.html',
    controller: 'SearchResultsController'
  });

  // configure html5 to get links working on jsfiddle
  $locationProvider
    .html5Mode(false);
});