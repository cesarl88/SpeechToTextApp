(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = [ '$scope','$location', '$rootScope', '$http','$cookies'];
    function HomeController($scope,$location, $rootScope, $http,$cookies) {
        var vm = this;
        $scope.Files = []
        vm.home = home;
        console.log($rootScope.globals)

        vm.home();

        $scope.edit = function (file)
        {
            console.log('To edit')
            console.log(file)
        }

        function home() {
            vm.dataLoading = true;

            console.log($rootScope.globals.currentUser.token);
            $http.get('http://localhost:8000/account-files/files/', {
                headers : 
                {
                    'authorization' : 'Token ' + $rootScope.globals.currentUser.token
                }
            }).then(function (response) {
                    console.log(response.data)
                    $scope.Files = response.data;
               }, function (response) {
                
            });

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