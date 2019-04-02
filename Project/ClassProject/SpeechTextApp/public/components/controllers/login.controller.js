(function () {
    'use strict';

    angular
        .module('app')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location','$cookies', 'AuthenticationService'];
    function LoginController($location, $cookies, AuthenticationService, FlashService) {
        var vm = this;

        console.log("Login Controller")

        vm.login = login;

        (function initController() {
            // reset login status
            AuthenticationService.ClearCredentials();
            console.log('init LoginController')
        })();

        function login() {
            console.log('I just clicked Log in')
            vm.dataLoading = true;
            AuthenticationService.Login(vm.username, vm.password, function (response) {
                console.log(response.data)
                if (response.status == 200) {
                    AuthenticationService.SetCredentials(vm.username, vm.password,response.data.user.id, response.data.token, response.data.user.first_name, response.data.user.last_name, response.data.user.email);
                    $location.path('/home');
                } else {
                    vm.dataLoading = false;
                }
            });
        };
    }

})();