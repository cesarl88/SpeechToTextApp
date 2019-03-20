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
                    $cookies.put('Token', response.data.token)
                    console.log(response.data.token)
                    console.log($cookies.get('Token'))
                    AuthenticationService.SetCredentials(vm.username, vm.password, response.data.token);
                    $location.path('/home');
                } else {
                    
                    //FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
        };
    }

})();