(function () {
        'use strict';
    
        angular
            .module('app')
            .controller('DashboardController', DashboardController);
    
        DashboardController.$inject = [ '$location', '$rootScope', '$http'];
        function DashboardController($location, $rootScope, $http) {
            var vm = this;
    
            vm.dashboard = Dashboard;
            vm.startAudio = startAudio;
            vm.startVideo = startVideo;
            vm.startMic = startMic;
    
            function startAudio ()
            { $location.path('/TranscriptAudio/-1')}
            function startVideo ()
            { $location.path('/TranscriptVideo/-1')}
            function startMic ()
            { $location.path('/TranscriptMic/-1')}

            function Dashboard() {
                vm.dataLoading = true;
    
                 $http.post('http://speech-backend.herokuapp.com/account/Dashboard/', { username: vm.username, password: vm.password, first_name : vm.first_name, last_name: vm.last_name, email: vm.email})//, config)
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