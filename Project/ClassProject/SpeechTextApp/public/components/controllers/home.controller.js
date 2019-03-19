(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = [ '$location', '$rootScope', '$http'];
    function HomeController($location, $rootScope, $http) {
        var vm = this;

        vm.home = home;
        console.log('In home')
        vm.transcript = function ()
        {
            console.log('Hey going to transcript')
            $location.path("/dashboard")   
        }

        vm.about = function ()
        {
            console.log('Hey going to about')
            $location.path("/about")   
        }

        vm.profile = function ()
        {
            console.log('Hey going to profile')
            $location.path("/profile")   
        }

        function home() {
            vm.dataLoading = true;

            
            
            //  $http.post('http://localhost:8000/account/files/', { username: vm.username, password: vm.password, first_name : vm.first_name, last_name: vm.last_name, email: vm.email})//, config)
            //    .then(function (response) {
            //        console.log('Called home')
            //        console.log(response)
                   
            //        //Store token DO NOT FORGET THIS PART
            //        $location.path('/home');
            //        //callback(response);
            //    }, function (response) {
            //     console.log("Error on home " + response)
            //     //callback(response);
            // });

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