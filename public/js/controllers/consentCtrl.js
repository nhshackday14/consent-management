angular.module('consentApp')
.controller('SearchController',['$scope', '$location', 'slugify',
 function($scope, $location, slugify) {
     // Unicode (non-control) characters in the Latin-1 Supplement and Latin
     // Extended-A blocks, transliterated into ASCII characters.
  $scope.submit = function(){
    if($scope.text){
      $location.path('/procedure/' + slugify($scope.text));
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
