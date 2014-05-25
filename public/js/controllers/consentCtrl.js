angular.module('consentApp')
.controller('SearchController',['$scope', '$location',
 function($scope, $location) {
  $scope.submit = function(){
    if($scope.text){
      $location.path('search/' + $scope.text);
    }
  };

}])
.controller('SearchResultsController',['$scope', '$routeParams', 'Procedures',
 function($scope, $routeParams, Procedures) {
  $scope.query = $routeParams.query;
  $scope.procedures = Procedures.query({query: $routeParams.query});
}])
.controller('ConsentFormController',['$scope', '$routeParams', 'ConsentForm',
 function($scope, $routeParams, ConsentForm) {
  var consentForm = ConsentForm.query({id: $routeParams.id}, function() {
    $scope.consentForm = consentForm;
    $scope.consentFormExists = consentForm.consent_form === null ? "false" : "true";
  });
}]);