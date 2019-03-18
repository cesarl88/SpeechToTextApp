(function () {
        'use strict';
    
        angular
            .module('app')
            .controller('DashboardController', DashboardController);
    
        DashboardController.$inject = [ '$location', '$rootScope', '$http'];
        function DashboardController($location, $rootScope, $http) {
            var vm = this;
    
            vm.dashboard = Dashboard;
    
            function Dashboard() {
                vm.dataLoading = true;
    
                 $http.post('http://localhost:8000/account/Dashboard/', { username: vm.username, password: vm.password, first_name : vm.first_name, last_name: vm.last_name, email: vm.email})//, config)
                   .then(function (response) {
                       console.log('Called Dashboard')
                       console.log(response)
                       
                       //Store token DO NOT FORGET THIS PART
                       $location.path('/dashboard');
                       //callback(response);
                   }, function (response) {
                    console.log("Error on Dashboard " + response)
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