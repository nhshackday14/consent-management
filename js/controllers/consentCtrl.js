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
    $scope.procedures = Procedures.query({query: $routeParams.query});
}])
.controller('ConsentFormController',['$scope', '$routeParams', 'ConsentForm',
   function($scope, $routeParams, ConsentForm) {
    $scope.consentForm = ConsentForm.query({id: $routeParams.id});
}]);