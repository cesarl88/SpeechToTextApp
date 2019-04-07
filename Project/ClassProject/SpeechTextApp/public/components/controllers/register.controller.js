(function () {
    'use strict';

    angular
        .module('app')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = [ '$location', '$rootScope', '$http'];
    function RegisterController($location, $rootScope, $http) {
        var vm = this;

        vm.register = register;

        function register() {
            vm.dataLoading = true;

             $http.post('http://speech-backend.herokuapp.com/account/register/', { username: vm.username, password: vm.password, first_name : vm.first_name, last_name: vm.last_name, email: vm.email})//, config)
               .then(function (response) {
                   console.log('Called register')
                   console.log(response)
                   
                   //Store token DO NOT FORGET THIS PART
                   $location.path('/home');
                   //callback(response);
               }, function (response) {
                console.log("Error on register " + response)
                //callback(response);
            });

            // UserService.Create(vm.user)
            //     .then(function (response) {
            //         if (response.success) {
            //             FlashService.Success('Registration successful', true);
            //             $location.path('/login');
            //         } else {
            //             FlashService.Error(response.message);
            //             vm.dataLoading = false;
            //         }
            //     });
        }
    }

})();