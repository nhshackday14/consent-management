angular.module('consentApp', ['ngRoute', 'ngResource'])

.config(function($routeProvider, $locationProvider) {
  $routeProvider
   .when('/search', {
    templateUrl: 'templates/searchResults.html',
    controller: 'SearchResultsController'
  }).when('/consent_form/:id', {
    templateUrl: 'templates/consentForm.html',
    controller: 'ConsentFormController'
  });

  // configure html5 to get links working on jsfiddle
  $locationProvider
    .html5Mode(false);
});