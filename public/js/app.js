angular.module('consentApp', ['ngRoute', 'ngResource'])

.config(function($routeProvider, $locationProvider) {
  $routeProvider
  .when('/', {
    templateUrl: '/static/templates/search.html',
    controller: 'SearchController'
  })
  .when('/about', {
    templateUrl: '/static/templates/about.html'
  })
  .when('/search/:query', {
    templateUrl: '/static/templates/searchResults.html',
    controller: 'SearchResultsController'
  })
  .when('/consent-form/:id', {
    templateUrl: '/static/templates/consentForm.html',
    controller: 'ConsentFormController'
  });

  // configure html5 to get links working on jsfiddle
  $locationProvider
    .html5Mode(false);
});
