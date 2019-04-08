(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = [ '$scope','$location', '$rootScope', '$http','$cookies', 'SweetAlert', 'NgTableParams'];
    function HomeController($scope,$location, $rootScope, $http, $cookies, SweetAlert,NgTableParams) {
        var vm = this;
        $scope.Files = []
        $scope.search = ''
        ///vm.home = home;
        console.log($rootScope.globals)

        

        $scope.edit = function (file)
        {
            console.log('To edit')
            console.log(file)

            if(file.Type == 1)
            {
                console.log('Audio File')
                $location.path('TranscriptAudio/' + file.id)
            }
            else if(file.Type == 2)
            {
                console.log('Video File')
                $location.path('TranscriptVideo/' + file.id)
            }
            else if(file.Type == 3)
            {
                console.log('Microphone File')
                $location.path('TranscriptMic/' + file.id)
            }
            else
            { alert('File type not recognized'); }
        }

        $scope.Delete = function(file)
        {
            var r =  confirm("Do you want to delete " + file.Name + '?')
            if(r == true)
            { 
                $http.delete('http://speech-backend.herokuapp.com/account-files/files-delete/' + file.id + '/', {
                    headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token} 
                }).then(function (response) {
                        alert(file.Name + ' has been deleted')
                        vm.home();
                   }, function (response) {
                    alert('Error deleting ' + file.Name)
                   });
                
            }
            else
            {
                alert('Cancelled')
            }
        }

        $scope.filterFiles = function()
        {
            if($scope.search == '')
            { vm.home();}
            else
            {
                $http.get('http://speech-backend.herokuapp.com/account-files/files/?q=' + $scope.search, {
                headers : 
                {
                    'authorization' : 'Token ' + $rootScope.globals.currentUser.token
                }
            }).then(function (response) {
                    console.log(response.data)
                    $scope.Files = response.data;
                    $scope.filesTable = new NgTableParams({

                        page: 1,
                        
                        count: 5
                        
                        },  { dataset: $scope.Files });
               }, function (response) {
                
            });

            }

        }
        $scope.home = function() {
            vm.dataLoading = true;

            console.log($rootScope.globals.currentUser.token);
            $http.get('http://speech-backend.herokuapp.com/account-files/files/', {
                headers : 
                {
                    'authorization' : 'Token ' + $rootScope.globals.currentUser.token
                }
            }).then(function (response) {
                    console.log(response.data)
                    $scope.Files = response.data;
                    $scope.filesTable = new NgTableParams({

                        page: 1,
                        
                        count: 5
                        
                        },  { dataset: $scope.Files });
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
        $scope.home();
    }

})();