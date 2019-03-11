(function () {
    'use strict';

    angular
        .module('app')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', 'AuthenticationService'];
    function LoginController($location, AuthenticationService, FlashService) {
        var vm = this;

        console.log("Login Controller")

        vm.login = login;

        (function initController() {
            // reset login status
            AuthenticationService.ClearCredentials();
        })();

        function login() {
            console.log('I just clicked Log in')
            vm.dataLoading = true;
            AuthenticationService.Login(vm.username, vm.password, function (response) {
                console.log(response.data)
                if (response.status == 200) {
                    AuthenticationService.SetCredentials(vm.username, vm.password, response.token);
                    $location.path('/');
                } else {
                    
                    //FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
        };
    }

})();