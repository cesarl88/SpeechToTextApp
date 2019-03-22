(function () {
    'use strict';

    angular
        .module('app')
        .controller('profileController', profileController);

        profileController.$inject = [ '$scope','$location', '$rootScope', '$http','$cookies'];
    function profileController($scope,$location, $rootScope, $http,$cookies) {
        $scope.Files = []
        $scope.passwordError = false
        $scope.name_Error = false
        $scope.last_name_Error = false
        $scope.email_Error = false
        $scope.goodtogo = false
        $scope.EditInfo= function () {
 
            $scope.goodtogo = false
            $scope.data = {}

            console.log($scope.first_name)
            console.log($scope.last_name)
            console.log($scope.email)

            if(typeof $scope.first_name !== 'undefined' && $scope.first_name != '')
            { 
                if($scope.first_name == $scope.first_name_confirm)
                {
                    $scope.data['first_name'] =  $scope.first_name
                    $scope.goodtogo = true
                    $scope.name_Error = false
                }
                else
                {
                    $scope.name_Error = true
                    return
                }
                
            }
            else
            {$scope.name_Error = false}
            if(typeof $scope.last_name !== 'undefined' && $scope.last_name != '')
            { 
                if($scope.last_name == $scope.last_name_confirm)
                {
                    $scope.data['last_name'] =  $scope.last_name
                    $scope.goodtogo = true
                    $scope.last_name_Error = false
                }
                else
                {
                    $scope.last_name_Error = true
                    return
                }
            }
            else
            {$scope.last_name_Error = false}
            if(typeof $scope.email !== 'undefined' && $scope.email != '')
            {
                if($scope.email == $scope.email_confirm)
                {
                    $scope.data['email'] =  $scope.email
                    $scope.goodtogo = true
                    $scope.email_Error = false
                }
                else
                {
                    $scope.email_Error = true
                    return
                }
            }
            else
            {$scope.email_Error = false}

            if($scope.goodtogo)
            {

                console.log($scope.data)
                $http.put('http://localhost:8000/account/update-profile/' + $rootScope.globals.currentUser.id + '/', 
                $scope.data ,
                    {
                        headers : 
                        {
                            'authorization' : 'Token ' + $rootScope.globals.currentUser.token
                        }
                    }).then(function (response) {
                        if($scope.data['first_name']){
                            $rootScope.globals.currentUser.first_name = $scope.data['first_name']
                        }
                        if($scope.data['last_name']){
                            $rootScope.globals.currentUser.last_name = $scope.data['last_name']
                        }
                        if($scope.data['email']){
                            $rootScope.globals.currentUser.email = $scope.data['email']
                        }
                        var cookieExp = new Date();
                        cookieExp.setDate(cookieExp.getDate() + 7);
                        $cookies.putObject('globals', $rootScope.globals, { expires: cookieExp });
                        $location.path('/home');
                        //callback(response);
                    }, function (response) {
                        //Show error modal
                    console.log("Error on home " + response)
                    //callback(response);
                });
            }
            else
            { alert('Nothing to modify.')}


            
            
        }

        $scope.EditPassword = function () {
            
            if($scope.newPassword != $scope.confirmPassword)
            { $scope.passwordError = true; }
            else
            {
                $http.post('http://localhost:8000/account/update-password/', 
                { 
                    Password : $scope.Password, 
                    newPassword: $scope.newPassword, 
                    confirmPassword: $scope.confirmPassword},{
                       headers : 
                       {
                           'authorization' : 'Token ' + $rootScope.globals.currentUser.token
                       }
                   })
                  .then(function (response) {
                      
                      $location.path('/home');
                      $scope.passwordError = false
                      //callback(response);
                  }, function (response) {
                    console.log(response.data)
                   //Show a modal
                    alert(response.data.error)
                   //callback(response);
               });
            }

             

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