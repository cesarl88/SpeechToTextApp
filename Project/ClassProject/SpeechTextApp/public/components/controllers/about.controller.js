(function () {
    'use strict';

    angular
        .module('app')
        .controller('AboutController', AboutController);

    aboutController.$inject = [ '$location', '$rootScope', '$http'];
    function aboutController($location, $rootScope, $http) {
        var vm = this;

        vm.about = About;

        function About() {
            vm.dataLoading = true;

             $http.post('http://localhost:8000/account/About/', { username: vm.username, password: vm.password, first_name : vm.first_name, last_name: vm.last_name, email: vm.email})//, config)
               .then(function (response) {
                   console.log('Called About')
                   console.log(response)
                   
                   //Store token DO NOT FORGET THIS PART
                   $location.path('/about');
                   //callback(response);
               }, function (response) {
                console.log("Error on About " + response)
                //callback(response);
            })
        }
    }

})();