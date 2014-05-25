'use strict';

/* Services */

var consentServices = angular.module('consentApp')
.factory('Procedures', ['$resource',
  function($resource){
    return $resource('/api-1/procedures/?q=:query&format=json', {}, {
      query: {method:'GET', isArray:true}
    });
  }])
.factory('ConsentForm', ['$resource',
  function($resource){
    return $resource('/api-1/procedures/:id?format=json', {}, {
      query: {method:'GET', isArray:false}
    });
  }]);