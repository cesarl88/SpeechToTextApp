(function () {
    'use strict';

    var app = angular
        .module('app', ['ngCookies', 'oc.lazyLoad', 'appRoutes', 'oitozero.ngSweetAlert', 'ngFileUpload', 'ngTable', 'uuid'])
        //.config(config)
        .run(run);

    //AppController.$inject = ['$scope', '$rootScope'];
    app.controller('AppController', ['$scope', '$rootScope','$location', '$cookies', '$http',
    function ($scope, $rootScope, $location, $cookies, $http) {
        var vm = this;
        $scope.IsLogin = false;
        //$scope.Title = 'Speecth'
        
        console.log('In home')
        $scope.transcript = function ()
        {
            console.log('Hey going to transcript')
            $location.path("/dashboard")   
        }

        $scope.about = function ()
        {
            console.log('Hey going to about')
            $location.path("/about")   
        }

        $scope.profile = function ()
        {
            console.log('Hey going to profile')
            $location.path("/profile")   
        }

        $scope.logout = function()
        {
            console.log($rootScope.globals.currentUser.token)
            $http.post('http://speech-backend.herokuapp.com/account/logout/', {},{
                headers : 
                {
                    'authorization' : 'Token ' + $rootScope.globals.currentUser.token
                }
            }).then(function (response) {
                console.log("Login out")
                $location.path('/login');
                $rootScope.globals = {};
                $cookies.remove('globals');
               }, function (response) {
                console.log("Error on login " + response.data)
            });

            
        }

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in and trying to access a restricted page
            //var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
            var loggedIn = $rootScope.globals.currentUser;
            console.log(loggedIn)
            if ((typeof loggedIn == 'undefined'))
            {
                console.log('Inside If')
                if($location.path() != '/register')
                { $location.path('/login');}

                $scope.IsLogin = false;
                $scope.ShowSideMenu =  false
                
            }
            else
            {
                $scope.ShowSideMenu = true
                $scope.IsLogin = true;
                console.log('Inside else')
            }
            
        });

        
    }]);
    //config.$inject = ['$routeProvider', '$locationProvider'];
    // function config($routeProvider, $locationProvider) {
    //     $routeProvider
    //         .when('/', {
    //             controller: 'HomeController',
    //             templateUrl: 'public/components/templates/home.view.html',
    //             controllerAs: 'vm'
    //         })

    //         .when('/login', {
    //             controller: 'LoginController',
    //             templateUrl: 'public/components/templates/login.view.html',
    //             controllerAs: 'vm'
    //         })

    //         .when('/register', {
    //             controller: 'RegisterController',
    //             templateUrl: 'public/components/templates/register.view.html',
    //             controllerAs: 'vm'
    //         })
    //         .otherwise({ redirectTo: '/login' });
    // }

    run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
    function run($rootScope, $location, $cookies, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookies.getObject('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata;
        }

        // $rootScope.$on('$locationChangeStart', function (event, next, current) {
        //     // redirect to login page if not logged in and trying to access a restricted page
        //     var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
        //     var loggedIn = $rootScope.globals.currentUser;
        //     if (restrictedPage && !loggedIn) {
        //         $location.path('/login');
        //     }
        // });
    }

})();