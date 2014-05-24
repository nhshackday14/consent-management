angular.module('consentApp').controller('SearchResultsController',['$scope', 'Procedures',
 function($scope, Procedures) {
    $scope.procedures = Procedures.query();
}])
.controller('ConsentFormController',['$scope', '$routeParams', 'ConsentForm',
 function($scope, $routeParams, ConsentForm) {
    $scope.consentForm = ConsentForm.query({id: $routeParams.id});
}]);