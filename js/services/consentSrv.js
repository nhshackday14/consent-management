'use strict';

/* Services */

var consentServices = angular.module('consentApp', ['ngResource']);

consentServices.factory('Procedures', ['$resource',
  function($resource){
    return $resource('procedures', {}, {
      query: {method:'GET', params:{id:1}, isArray:true}
    });
  }]);