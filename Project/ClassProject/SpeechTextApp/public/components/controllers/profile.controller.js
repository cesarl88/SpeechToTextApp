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
        
        $scope.EditInfo= function () {

            
        }

        $scope.EditPassword = function () {
            
             $http.post('http://localhost:8000/account/files/', 
             { 
                 password : vm.password, 
                 newPassword: vm.newPassword, 
                 confirmPassword: vm.confirmPassword},{
                    headers : 
                    {
                        'authorization' : 'Token ' + $cookies.get('Token')
                    }
                })
               .then(function (response) {
                   
                   $location.path('/home');
                   //callback(response);
               }, function (response) {
                console.log("Error on home " + response)
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