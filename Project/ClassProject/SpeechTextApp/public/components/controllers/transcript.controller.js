(function () {
    'use strict';

    angular
        .module('app')
        .controller('TranscriptController', TranscriptController);

    TranscriptController.$inject = [ '$location', '$rootScope', '$http', '$state', '$scope', 'Upload'];
    function TranscriptController($location, $rootScope, $http, $state, $scope, Upload) {
        $scope.File = { 
            id : -1,
            Name : '',
            Transcript : '',
            Comment : '',
            Content :''

        }

        $scope.myFile = null
        $scope.IsNew = false

        this.rec = new webkitSpeechRecognition();
        this.interim = [];
        this.final = '';
        var self = this;
        
        this.rec.continuous = true;
        this.rec.lang = 'en-US';
        this.rec.interimResults = true;
        $scope.Inprogress = false

        this.rec.onerror = function(event) {
            console.log('error!');
        };
        

        this.rec.onresult = function(event) {
            for(var i = event.resultIndex; i < event.results.length; i++) {
              if(event.results[i].isFinal) {
                self.final = self.final.concat(event.results[i][0].transcript);
                $scope.File.Transcript = self.final
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
                        self.final = ' ' +  $scope.File.Transcript
                        console.log($scope.File)
                    }
               }, function (response) {
                
            });
        }

        $scope.stop = function()
        {
            $scope.Inprogress = false
            self.rec.stop();

        }
        $scope.start = function()
        {
            function Transcript(offset)
            {
                var data = { id: $state.params.id, offset:  offset}

                console.log(data)
                $http.post('http://localhost:8000/account-files/files-transcript/' + $state.params.id + '/', data, { 
                    headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token } 
                }
                ).then(function (response) {
                    console.log(response)
                    if(response.status == 201)
                    { $scope.File.Transcript = response.data }
                    else if(response.status == 200)
                    { 
                        $scope.File.Transcript = response.data
                        Transcript(offset + 30)
                    }
                    else
                    { alert('Error processing the request')}
                }, function (response) {
                    
                    console.log("Error on About ")
                    console.log(response)
                    
                });

            }
            if($scope.File.Type != 3)
            {
                Transcript(0);
            }
            else
            {
                $scope.Inprogress = true
                self.rec.start();
            }
        
        }
        $scope.download = function()
        {

            if(!$scope.File.Transcript) {
                console.error('Console.save: No data')
                return;
                }
        
                var filename = $scope.File.Name + uuidv4() + '.txt'
        
                var blob = new Blob([$scope.File.Transcript], {type: 'text/plain'}),
                    e    = document.createEvent('MouseEvents'),
                    a    = document.createElement('a')
            // FOR IE:
            
            if (window.navigator && window.navigator.msSaveOrOpenBlob) {
                window.navigator.msSaveOrOpenBlob(blob, filename);
            }
            else{
                var e = document.createEvent('MouseEvents'),
                    a = document.createElement('a');
            
                a.download = filename;
                a.href = window.URL.createObjectURL(blob);
                a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':');
                e.initEvent('click', true, false, window,
                    0, 0, 0, 0, 0, false, false, false, false, 0, null);
                a.dispatchEvent(e);
            }
        }


        $scope.save = function()
        {

            if($scope.IsNew)
            {
                if($location.path().indexOf('/TranscriptMic/') !== -1)
                {
                    var data = {
                        "Comment" : $scope.File.Comment,
                        "Name" : $scope.File.Name,
                        "Type" : 3
                    }
                    console.log(data)
        
                    $http.post('http://127.0.0.1:8000/account-files/files/', data,{ 
                        headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token } 
                    }
                    ).then(function (response) {
                        console.log(response)
                        $location.path('/TranscriptMic/'+ response.data.id)
                    }, function (response) {
                        console.log("Error on About " + response)
                    
                    });

                }
                else if($scope.myFile)
                {
                    var type =  1
                    console.log($location.path())
                    if($location.path().indexOf('/TranscriptVideo/') !== -1)
                    { type = 2 }
                    
                    var data =  {
                        Content : $scope.myFile, 
                        Name: $scope.File.Name,
                        Comment: $scope.File.Comment,
                        Type: type
                    }
                    console.log(data)
                    Upload.upload({
                        url: 'http://127.0.0.1:8000/account-files/files/',
                        data : data,
                        headers : { 'authorization' : 'Token ' + $rootScope.globals.currentUser.token }
                    }).then(function (response) {
                        console.log('Success ' + response.config.data.Content.name + 'uploaded. Response: ');
                        console.log(response.data)
                            if(response.data.Type == 1)
                            {$location.path('/TranscriptAudio/' + response.data.id)}
                            else if(response.data.Type == 2)
                            {$location.path('/TranscriptVideo/'+ response.data.id)}
                            
                    }, function (resp) {
                        console.log('Error status: ' + resp.status);
                    }, function (evt) {
                        var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                        console.log(evt)
                        console.log('progress: ' + progressPercentage + '% ' + evt.config.data.Content.name);
                    });

                }
                else
                {
                    alert('File undefined');
                }
                
    
                
            }
            else
            {
                
                var data = {
                    "Comment" : $scope.File.Comment,
                    "Name" : $scope.File.Name
                }

                if($scope.File.Type == 3)
                { data["Transcript"] = $scope.File.Transcript}

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
            
        }  

        if($state.params.id < 1)
        { $scope.IsNew = true}
        else
        { $scope.GetFile(); }
        
        $scope.$watch('myFile', function (newVal) {
            if (newVal)
              console.log(newVal);
          });

        
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