angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'home',
        url: '/home',
        templateUrl: 'public/components/templates/home.view.html',
        controller: 'HomeController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/home.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'login',
        url: '/login',
        templateUrl: 'public/components/templates/login.view.html',
        controller: 'LoginController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/login.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'register',
        url: '/register',
        templateUrl: 'public/components/templates/register.view.html',
        controller: 'RegisterController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/register.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'dashboard',
        url: '/dashboard',
        templateUrl: 'public/components/templates/dashboard.html',
        controller: 'DashboardController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/dashboard.controller.js'
                    ]
                });
            }]

        }
    });

    $urlRouterProvider.otherwise('/');
}]);