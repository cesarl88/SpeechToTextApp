(function () {
    'use strict';

    angular
        .module('app')
        .controller('TranscriptController', TranscriptController);

    TranscriptController.$inject = [ '$location', '$rootScope', '$http', '$state', '$scope'];
    function TranscriptController($location, $rootScope, $http, $state, $scope) {
        $rootScope.File = {}
        this.rec = new webkitSpeechRecognition();
        this.interim = [];
        this.final = '';
        var self = this;
        
        this.rec.continuous = false;
        this.rec.lang = 'en-US';
        this.rec.interimResults = true;

        this.rec.onerror = function(event) {
            console.log('error!');
        };
        

        this.rec.onresult = function(event) {
            for(var i = event.resultIndex; i < event.results.length; i++) {
              if(event.results[i].isFinal) {
                self.final = self.final.concat(event.results[i][0].transcript);
                console.log(event.results[i][0].transcript);
                $scope.$apply();
              } else {
                self.interim.push(event.results[i][0].transcript);
                console.log('interim ' + event.results[i][0].transcript);
                $scope.$apply();
              }
            }
          };

        $rootScope.GetFile = function()
        {
            console.log($rootScope.globals.currentUser.token);
            console.log($state.params.id);
            $http.get('http://localhost:8000/account-files/files/' + $state.params.id + '/', {
                headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token }
            }).then(function (response) {
                    console.log(response.data)
                    if(response.data.length > 0)
                    {
                        $scope.File = response.data[0];
                        console.log($scope.File)
                    }
               }, function (response) {
                
            });

        }

        
        $scope.start = function()
        {
            if($scope.File.Type != 3)
            {
                var data = { "id" : $state.params.id}
                console.log(data)
    
                $http.post('http://localhost:8000/account-files/files-transcript/' + $state.params.id + '/', data, { 
                    headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token } 
                }
                ).then(function (response) {
                    console.log(response)
                    $scope.File.Transcript = response.data
                }, function (response) {
                    
                    console.log("Error on About ")
                    console.log(response)
                    
                });

            }
            else
            {self.rec.start();}
        
        }

        $scope.save = function()
        {
            var data = {
                "Comment" : $scope.File.Comment,
                "Name" : $scope.File.Name
            }
            console.log(data)

            $http.put('http://localhost:8000/account-files/files-update/' + $state.params.id + '/', data, { 
                headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token } 
            }
            ).then(function (response) {
                console.log(response)
                
                //Store token DO NOT FORGET THIS PART
                $location.path('/HOME');
                //callback(response);
            }, function (response) {
                console.log("Error on About " + response)
            
            });
        }  

        

        $scope.GetFile();
        // function About() {
        //     vm.dataLoading = true;

        //      $http.post('http://localhost:8000/account/About/', { username: vm.username, password: vm.password, first_name : vm.first_name, last_name: vm.last_name, email: vm.email})//, config)
        //        .then(function (response) {
        //            console.log('Called About')
        //            console.log(response)
                   
        //            //Store token DO NOT FORGET THIS PART
        //            $location.path('/about');
        //            //callback(response);
        //        }, function (response) {
        //         console.log("Error on About " + response)
        //         //callback(response);
        //     })
        // }
    }

})();