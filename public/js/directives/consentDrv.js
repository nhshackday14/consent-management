angular.module('consentApp').directive('typeahead', ['$rootScope','$location', 'slugify', function($rootScope, $location, slugify) {
  return {
    restrict: 'A',
    link: function(scope, element, attrs) {
      element.typeahead({
        minLength: 3,
        highlight: true
      },{
        name: 'procedure-dataset',
        source: function(query, cb) {
          $.getJSON('/api-1/procedures/?q='+ query +'&format=json', function(result) {
            cb(result);
          });
        },
        displayKey: 'name'
      });

      element.on('typeahead:selected', function(e, model) {
        element.val($(this).val());
        scope.text = $(this).val();
        $rootScope.$apply(function() {
          $location.path('procedure/' + slugify(scope.text));
        });
      });
    }
  };
}]);
