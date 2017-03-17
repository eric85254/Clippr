Search.setIndex({docnames:["Clipper_V_0","administration","api","core","core.management","core.management.commands","core.migrations","core.utils","customer","customer.management","customer.management.commands","customer.utils","index","manage","setup","stylist","stylist.management","stylist.management.commands","stylist.migrations","stylist.utils"],envversion:51,filenames:["Clipper_V_0.rst","administration.rst","api.rst","core.rst","core.management.rst","core.management.commands.rst","core.migrations.rst","core.utils.rst","customer.rst","customer.management.rst","customer.management.commands.rst","customer.utils.rst","index.rst","manage.rst","setup.rst","stylist.rst","stylist.management.rst","stylist.management.commands.rst","stylist.migrations.rst","stylist.utils.rst"],objects:{"":{Clipper_V_0:[0,0,0,"-"],administration:[1,0,0,"-"],api:[2,0,0,"-"],core:[3,0,0,"-"],customer:[8,0,0,"-"],manage:[13,0,0,"-"],setup:[14,0,0,"-"],stylist:[15,0,0,"-"]},"administration.apps":{AdministrationConfig:[1,1,1,""]},"administration.apps.AdministrationConfig":{name:[1,2,1,""]},"administration.views":{approve_applicant:[1,3,1,""],profile:[1,3,1,""],reinstate_application:[1,3,1,""],reject_applicant:[1,3,1,""],schedule_interview:[1,3,1,""],view_interviews:[1,3,1,""],view_rejects:[1,3,1,""],view_stylist_applications:[1,3,1,""],view_stylists:[1,3,1,""]},"api.apps":{ApiConfig:[2,1,1,""]},"api.apps.ApiConfig":{name:[2,2,1,""]},"api.backends":{CsrfExemptSessionAuthentication:[2,1,1,""]},"api.backends.CsrfExemptSessionAuthentication":{enforce_csrf:[2,4,1,""]},"api.permissions":{IsCurrentUserOrSuperUser:[2,1,1,""],IsOwnerOfAppointment:[2,1,1,""],IsOwnerOfHaircut:[2,1,1,""],IsUserLoggedIn:[2,1,1,""],OnlySuperUsersCanModify:[2,1,1,""]},"api.permissions.IsCurrentUserOrSuperUser":{has_object_permission:[2,4,1,""]},"api.permissions.IsOwnerOfAppointment":{has_object_permission:[2,4,1,""],has_permission:[2,4,1,""]},"api.permissions.IsOwnerOfHaircut":{has_object_permission:[2,4,1,""],has_permission:[2,4,1,""]},"api.permissions.IsUserLoggedIn":{has_permission:[2,4,1,""]},"api.permissions.OnlySuperUsersCanModify":{has_object_permission:[2,4,1,""],has_permission:[2,4,1,""]},"api.serializers":{AppointmentSerializer:[2,1,1,""],GlobalMenuSerializer:[2,1,1,""],PortfolioHaircutSerializer:[2,1,1,""],StylistMenuSerializer:[2,1,1,""],StylistSerializer:[2,1,1,""],UserSerializer:[2,1,1,""]},"api.serializers.AppointmentSerializer":{Meta:[2,1,1,""]},"api.serializers.AppointmentSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""]},"api.serializers.GlobalMenuSerializer":{Meta:[2,1,1,""]},"api.serializers.GlobalMenuSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""]},"api.serializers.PortfolioHaircutSerializer":{Meta:[2,1,1,""]},"api.serializers.PortfolioHaircutSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""]},"api.serializers.StylistMenuSerializer":{Meta:[2,1,1,""]},"api.serializers.StylistMenuSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""]},"api.serializers.StylistSerializer":{Meta:[2,1,1,""]},"api.serializers.StylistSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""]},"api.serializers.UserSerializer":{Meta:[2,1,1,""],create:[2,4,1,""]},"api.serializers.UserSerializer.Meta":{extra_kwargs:[2,2,1,""],fields:[2,2,1,""],model:[2,2,1,""]},"api.views":{AppointmentViewSet:[2,1,1,""],GlobalMenuViewSet:[2,1,1,""],HaircutViewSet:[2,1,1,""],StylistMenuViewSet:[2,1,1,""],StylistViewSet:[2,1,1,""],UserViewSet:[2,1,1,""],customer_rating:[2,3,1,""],stylist_rating:[2,3,1,""],stylist_search:[2,3,1,""],user_login:[2,3,1,""],user_logout:[2,3,1,""]},"api.views.AppointmentViewSet":{authentication_classes:[2,2,1,""],get_queryset:[2,4,1,""],perform_create:[2,4,1,""],permission_classes:[2,2,1,""],queryset:[2,2,1,""],serializer_class:[2,2,1,""],suffix:[2,2,1,""]},"api.views.GlobalMenuViewSet":{authentication_classes:[2,2,1,""],permission_classes:[2,2,1,""],queryset:[2,2,1,""],serializer_class:[2,2,1,""],suffix:[2,2,1,""]},"api.views.HaircutViewSet":{authentication_classes:[2,2,1,""],get_queryset:[2,4,1,""],perform_create:[2,4,1,""],permission_classes:[2,2,1,""],queryset:[2,2,1,""],serializer_class:[2,2,1,""],suffix:[2,2,1,""]},"api.views.StylistMenuViewSet":{get_queryset:[2,4,1,""],perform_create:[2,4,1,""],queryset:[2,2,1,""],serializer_class:[2,2,1,""],suffix:[2,2,1,""]},"api.views.StylistViewSet":{authentication_classes:[2,2,1,""],get_queryset:[2,4,1,""],permission_classes:[2,2,1,""],queryset:[2,2,1,""],serializer_class:[2,2,1,""],suffix:[2,2,1,""]},"api.views.UserViewSet":{authentication_classes:[2,2,1,""],get_queryset:[2,4,1,""],permission_classes:[2,2,1,""],queryset:[2,2,1,""],serializer_class:[2,2,1,""],suffix:[2,2,1,""]},"core.apps":{CoreConfig:[3,1,1,""]},"core.apps.CoreConfig":{name:[3,2,1,""]},"core.backends":{EmailPhoneNumberOrUsernameModelBackend:[3,1,1,""]},"core.backends.EmailPhoneNumberOrUsernameModelBackend":{authenticate:[3,4,1,""],get_user:[3,4,1,""]},"core.forms":{NewUserForm:[3,1,1,""],UserInformation:[3,1,1,""]},"core.forms.NewUserForm":{Meta:[3,1,1,""],base_fields:[3,2,1,""],declared_fields:[3,2,1,""],media:[3,2,1,""]},"core.forms.NewUserForm.Meta":{fields:[3,2,1,""],model:[3,2,1,""]},"core.forms.UserInformation":{Meta:[3,1,1,""],base_fields:[3,2,1,""],declared_fields:[3,2,1,""],is_valid:[3,4,1,""],media:[3,2,1,""]},"core.forms.UserInformation.Meta":{fields:[3,2,1,""],model:[3,2,1,""]},"core.management":{commands:[5,0,0,"-"]},"core.management.commands":{createDefaultUsers:[5,0,0,"-"],createGlobalMenuOption:[5,0,0,"-"]},"core.management.commands.createDefaultUsers":{Command:[5,1,1,""]},"core.management.commands.createDefaultUsers.Command":{handle:[5,4,1,""],help:[5,2,1,""]},"core.management.commands.createGlobalMenuOption":{Command:[5,1,1,""]},"core.management.commands.createGlobalMenuOption.Command":{handle:[5,4,1,""],help:[5,2,1,""]},"core.migrations":{"0001_initial":[6,0,0,"-"],"0002_auto_20170316_0030":[6,0,0,"-"]},"core.migrations.0001_initial":{Migration:[6,1,1,""]},"core.migrations.0001_initial.Migration":{dependencies:[6,2,1,""],initial:[6,2,1,""],operations:[6,2,1,""]},"core.migrations.0002_auto_20170316_0030":{Migration:[6,1,1,""]},"core.migrations.0002_auto_20170316_0030.Migration":{dependencies:[6,2,1,""],initial:[6,2,1,""],operations:[6,2,1,""]},"core.models":{AnsweredQuestionnaire:[3,1,1,""],Application:[3,1,1,""],Appointment:[3,1,1,""],GlobalMenu:[3,1,1,""],ItemInBill:[3,1,1,""],Questionnaire:[3,1,1,""],Review:[3,1,1,""],StylistMenu:[3,1,1,""],User:[3,1,1,""]},"core.models.AnsweredQuestionnaire":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],get_next_by_time:[3,4,1,""],get_previous_by_time:[3,4,1,""],id:[3,2,1,""],objects:[3,2,1,""],questionnaire:[3,2,1,""],questionnaire_id:[3,2,1,""],response:[3,2,1,""],time:[3,2,1,""],user:[3,2,1,""],user_id:[3,2,1,""]},"core.models.Application":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],applicant:[3,2,1,""],applicant_id:[3,2,1,""],application_status:[3,2,1,""],denied_reason:[3,2,1,""],id:[3,2,1,""],interview_time:[3,2,1,""],objects:[3,2,1,""],reason:[3,2,1,""]},"core.models.Appointment":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],STATUS_ACCEPTED:[3,2,1,""],STATUS_CHOICES:[3,2,1,""],STATUS_COMPLETED:[3,2,1,""],STATUS_DECLINED:[3,2,1,""],STATUS_PENDING:[3,2,1,""],STATUS_RECHEDULED_BYSTYLIST:[3,2,1,""],STATUS_RESCHEDULED_BYCUSTOMER:[3,2,1,""],appointment:[3,2,1,""],customer:[3,2,1,""],customer_id:[3,2,1,""],date:[3,2,1,""],get_next_by_date:[3,4,1,""],get_previous_by_date:[3,4,1,""],get_status_display:[3,4,1,""],id:[3,2,1,""],iteminbill_set:[3,2,1,""],location:[3,2,1,""],objects:[3,2,1,""],price:[3,2,1,""],status:[3,2,1,""],stylist:[3,2,1,""],stylist_id:[3,2,1,""]},"core.models.GlobalMenu":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],id:[3,2,1,""],modified_global:[3,2,1,""],name:[3,2,1,""],objects:[3,2,1,""],portfoliohaircut_set:[3,2,1,""],price:[3,2,1,""]},"core.models.ItemInBill":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],appointment:[3,2,1,""],appointment_id:[3,2,1,""],charged:[3,2,1,""],id:[3,2,1,""],item_custom:[3,2,1,""],item_menu:[3,2,1,""],item_menu_id:[3,2,1,""],item_portfolio:[3,2,1,""],item_portfolio_id:[3,2,1,""],objects:[3,2,1,""],price:[3,2,1,""]},"core.models.Questionnaire":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],answeredquestionnaire_set:[3,2,1,""],id:[3,2,1,""],objects:[3,2,1,""],question:[3,2,1,""]},"core.models.Review":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],appointment:[3,2,1,""],appointment_id:[3,2,1,""],customer_rating:[3,2,1,""],id:[3,2,1,""],objects:[3,2,1,""],stylist_rating:[3,2,1,""]},"core.models.StylistMenu":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],id:[3,2,1,""],item_menu:[3,2,1,""],modified_global:[3,2,1,""],modified_global_id:[3,2,1,""],name:[3,2,1,""],objects:[3,2,1,""],price:[3,2,1,""],stylist:[3,2,1,""],stylist_id:[3,2,1,""]},"core.models.User":{DoesNotExist:[3,5,1,""],MultipleObjectsReturned:[3,5,1,""],REQUIRED_FIELDS:[3,2,1,""],USERNAME_FIELD:[3,2,1,""],answeredquestionnaire_set:[3,2,1,""],application_set:[3,2,1,""],average_customer_rating:[3,2,1,""],average_stylist_rating:[3,2,1,""],biography:[3,2,1,""],customer:[3,2,1,""],deal_set:[3,2,1,""],get_next_by_date_joined:[3,4,1,""],get_previous_by_date_joined:[3,4,1,""],groups:[3,2,1,""],hair_type:[3,2,1,""],hidden_hair_type:[3,2,1,""],id:[3,2,1,""],is_stylist:[3,2,1,""],location:[3,2,1,""],logentry_set:[3,2,1,""],owner:[3,2,1,""],phone_number:[3,2,1,""],phone_regex:[3,2,1,""],portfoliohaircut_set:[3,2,1,""],profile_picture:[3,2,1,""],stylist:[3,2,1,""],user_permissions:[3,2,1,""]},"core.utils":{global_constants:[7,0,0,"-"],view_logic:[7,0,0,"-"]},"core.utils.view_logic":{CookieClearer:[7,1,1,""],UserLogic:[7,1,1,""]},"core.utils.view_logic.CookieClearer":{appointment_cookies:[7,6,1,""],clear:[7,6,1,""]},"core.utils.view_logic.UserLogic":{login:[7,6,1,""],redirect_to_dashboard:[7,6,1,""],retrieve_user:[7,6,1,""],update_average:[7,6,1,""],upload_picture:[7,6,1,""]},"core.views":{change_password:[3,3,1,""],create_user:[3,3,1,""],home:[3,3,1,""],home_login:[3,3,1,""],home_safety:[3,3,1,""],home_style:[3,3,1,""],home_stylist:[3,3,1,""],logout:[3,3,1,""],returning_user:[3,3,1,""],update_basic_information:[3,3,1,""],upload_picture:[3,3,1,""]},"customer.apps":{CustomerConfig:[8,1,1,""]},"customer.apps.CustomerConfig":{name:[8,2,1,""]},"customer.forms":{NewAppointmentForm:[8,1,1,""],StylistApplicationForm:[8,1,1,""]},"customer.forms.NewAppointmentForm":{Meta:[8,1,1,""],base_fields:[8,2,1,""],declared_fields:[8,2,1,""],media:[8,2,1,""]},"customer.forms.NewAppointmentForm.Meta":{fields:[8,2,1,""],model:[8,2,1,""]},"customer.forms.StylistApplicationForm":{Meta:[8,1,1,""],base_fields:[8,2,1,""],declared_fields:[8,2,1,""],media:[8,2,1,""]},"customer.forms.StylistApplicationForm.Meta":{fields:[8,2,1,""],model:[8,2,1,""]},"customer.management":{commands:[10,0,0,"-"]},"customer.management.commands":{createDefaultAppointment:[10,0,0,"-"]},"customer.management.commands.createDefaultAppointment":{Command:[10,1,1,""]},"customer.management.commands.createDefaultAppointment.Command":{handle:[10,4,1,""],help:[10,2,1,""]},"customer.utils":{view_logic:[11,0,0,"-"]},"customer.utils.view_logic":{CustomerLogic:[11,1,1,""]},"customer.utils.view_logic.CustomerLogic":{is_customer:[11,6,1,""],render_application_status:[11,7,1,""],render_dashboard:[11,7,1,""],retrieve_application:[11,6,1,""]},"customer.views":{accept_appointment:[8,3,1,""],become_stylist:[8,3,1,""],cancel_appointment:[8,3,1,""],catch_menu_choices:[8,3,1,""],create_appointment:[8,3,1,""],dashboard:[8,3,1,""],dashboard_real:[8,3,1,""],obtain_selected_haircut:[8,3,1,""],obtain_selected_menuOption:[8,3,1,""],obtain_stylist_profile:[8,3,1,""],profile:[8,3,1,""],profile_real:[8,3,1,""],reschedule_appointment:[8,3,1,""],search_real:[8,3,1,""],settings_real:[8,3,1,""],stylist_search:[8,3,1,""],submit_review:[8,3,1,""],view_bill:[8,3,1,""]},"stylist.apps":{StylistConfig:[15,1,1,""]},"stylist.apps.StylistConfig":{name:[15,2,1,""]},"stylist.forms":{MenuOptionForm:[15,1,1,""],NewPortfolioHaircutForm:[15,1,1,""]},"stylist.forms.MenuOptionForm":{Meta:[15,1,1,""],base_fields:[15,2,1,""],declared_fields:[15,2,1,""],media:[15,2,1,""]},"stylist.forms.MenuOptionForm.Meta":{fields:[15,2,1,""],model:[15,2,1,""]},"stylist.forms.NewPortfolioHaircutForm":{Meta:[15,1,1,""],base_fields:[15,2,1,""],declared_fields:[15,2,1,""],media:[15,2,1,""]},"stylist.forms.NewPortfolioHaircutForm.Meta":{fields:[15,2,1,""],model:[15,2,1,""]},"stylist.management":{commands:[17,0,0,"-"]},"stylist.management.commands":{createDefaultHaircuts:[17,0,0,"-"]},"stylist.management.commands.createDefaultHaircuts":{Command:[17,1,1,""]},"stylist.management.commands.createDefaultHaircuts.Command":{handle:[17,4,1,""],help:[17,2,1,""]},"stylist.migrations":{"0001_initial":[18,0,0,"-"]},"stylist.migrations.0001_initial":{Migration:[18,1,1,""]},"stylist.migrations.0001_initial.Migration":{dependencies:[18,2,1,""],initial:[18,2,1,""],operations:[18,2,1,""]},"stylist.models":{Deal:[15,1,1,""],PortfolioHaircut:[15,1,1,""]},"stylist.models.Deal":{DoesNotExist:[15,5,1,""],MultipleObjectsReturned:[15,5,1,""],description:[15,2,1,""],id:[15,2,1,""],objects:[15,2,1,""],price_modifier:[15,2,1,""],stylist:[15,2,1,""],stylist_id:[15,2,1,""]},"stylist.models.PortfolioHaircut":{DoesNotExist:[15,5,1,""],MultipleObjectsReturned:[15,5,1,""],description:[15,2,1,""],id:[15,2,1,""],item_portfolio:[15,2,1,""],menu_option:[15,2,1,""],menu_option_id:[15,2,1,""],name:[15,2,1,""],objects:[15,2,1,""],picture:[15,2,1,""],price:[15,2,1,""],stylist:[15,2,1,""],stylist_id:[15,2,1,""]},"stylist.utils":{view_logic:[19,0,0,"-"]},"stylist.utils.view_logic":{BillLogic:[19,1,1,""]},"stylist.utils.view_logic.BillLogic":{update_price:[19,6,1,""]},"stylist.views":{accept_appointment:[15,3,1,""],add_haircut:[15,3,1,""],add_item:[15,3,1,""],add_travel_fee:[15,3,1,""],appointments:[15,3,1,""],complete_appointment:[15,3,1,""],create_menu_option:[15,3,1,""],dashboard:[15,3,1,""],decline_appointment:[15,3,1,""],delete_item:[15,3,1,""],delete_menu_option:[15,3,1,""],delete_portfoliohaircut:[15,3,1,""],edit_menu_option:[15,3,1,""],edit_portfoliohaircut:[15,3,1,""],portfolio:[15,3,1,""],profile:[15,3,1,""],profile_test:[15,3,1,""],remove_menu_option:[15,3,1,""],reschedule_appointment:[15,3,1,""],select_menu_option:[15,3,1,""],submit_review:[15,3,1,""],transactions:[15,3,1,""],upload_haircut:[15,3,1,""],view_bill:[15,3,1,""]},Clipper_V_0:{settings:[0,0,0,"-"],urls:[0,0,0,"-"],wsgi:[0,0,0,"-"]},administration:{admin:[1,0,0,"-"],apps:[1,0,0,"-"],models:[1,0,0,"-"],tests:[1,0,0,"-"],urls:[1,0,0,"-"],views:[1,0,0,"-"]},api:{admin:[2,0,0,"-"],apps:[2,0,0,"-"],backends:[2,0,0,"-"],models:[2,0,0,"-"],permissions:[2,0,0,"-"],serializers:[2,0,0,"-"],tests:[2,0,0,"-"],urls:[2,0,0,"-"],views:[2,0,0,"-"]},core:{admin:[3,0,0,"-"],apps:[3,0,0,"-"],backends:[3,0,0,"-"],forms:[3,0,0,"-"],management:[4,0,0,"-"],migrations:[6,0,0,"-"],models:[3,0,0,"-"],tests:[3,0,0,"-"],urls:[3,0,0,"-"],utils:[7,0,0,"-"],views:[3,0,0,"-"]},customer:{admin:[8,0,0,"-"],apps:[8,0,0,"-"],forms:[8,0,0,"-"],management:[9,0,0,"-"],models:[8,0,0,"-"],tests:[8,0,0,"-"],urls:[8,0,0,"-"],utils:[11,0,0,"-"],views:[8,0,0,"-"]},setup:{apps_with_migrations:[14,8,1,""]},stylist:{admin:[15,0,0,"-"],apps:[15,0,0,"-"],forms:[15,0,0,"-"],management:[16,0,0,"-"],migrations:[18,0,0,"-"],models:[15,0,0,"-"],tests:[15,0,0,"-"],urls:[15,0,0,"-"],utils:[19,0,0,"-"],views:[15,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","function","Python function"],"4":["py","method","Python method"],"5":["py","exception","Python exception"],"6":["py","staticmethod","Python static method"],"7":["py","classmethod","Python class method"],"8":["py","data","Python data"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:function","4":"py:method","5":"py:exception","6":"py:staticmethod","7":"py:classmethod","8":"py:data"},terms:{"0001_initi":[3,12,15],"0002_auto_20170316_0030":[3,12],"0008_alter_user_username_max_length":6,"abstract":6,"class":[0,1,2,3,5,6,7,8,10,11,15,17,18,19],"default":[2,10,17],"function":0,"import":[0,3,15],"return":[3,15],"static":[7,11,19],"true":[2,6,18],For:0,One:2,The:[0,3,15],__first__:18,abstractus:3,accept:3,accept_appoint:[8,15],access:[3,15],accessor:[3,15],add:0,add_haircut:15,add_item:15,add_travel_fe:15,addfield:6,admin:[0,12],administr:12,administrationconfig:1,alia:[2,3,8,15],anoth:0,answeredquestionnair:[3,6],answeredquestionnaire_set:3,api:12,apiconfig:2,app:12,app_label:[6,18],app_modul:[1,2,3,8,15],app_nam:[1,2,3,8,15],appconfig:[1,2,3,8,15],applic:[0,3,6,8],applicant_id:3,application_set:3,application_statu:[3,6],appoint:[2,3,6,8,10,15,19],appointment_cooki:7,appointment_id:3,appointmentseri:2,appointmentviewset:2,approve_applic:1,apps_with_migr:14,arg:[2,3,5,10,17],as_view:0,assign:[3,15],attribut:[3,15],auth:[3,6],authent:[2,3],authentication_class:2,auto_id:[3,8,15],autofield:[6,18],average_customer_r:[3,6],average_stylist_r:[3,6],backend:12,base:[0,1,2,3,5,6,7,8,10,11,15,17,18,19],base_field:[3,8,15],basecommand:[5,10,17],basepermiss:2,basicauthent:2,become_stylist:8,below:[3,15],billlog:19,biographi:[3,6],blog:0,boi:2,booleanfield:6,built:[3,15],callabl:0,can:[3,15],cancel_appoint:8,catch_menu_choic:8,change_password:3,charfield:[3,6,8,15,18],charg:[3,6],child:[3,15],children:[3,15],classmethod:11,clear:7,clipper_v_0:12,clippr:2,com:[0,2],command:[3,4,8,9,15,16],complete_appoint:15,conf:0,config:[0,1,2,3,8,15],configur:0,content:12,contrib:[3,6],cookie_nam:7,cookieclear:7,core:[10,12,14,15,17,18],coreconfig:3,creat:[2,5,10,17],create_appoint:8,create_forward_many_to_many_manag:[3,15],create_menu_opt:15,create_us:3,createdefaultappoint:[8,9],createdefaulthaircut:[15,16],createdefaultus:[3,4],createglobalmenuopt:[3,4],createmodel:[6,18],csrfexemptsessionauthent:2,custom:[2,3,5,6,12],customer_id:3,customer_r:[2,3,6],customerconfig:8,customerlog:11,dashboard:[8,15],dashboard_r:8,data:[2,3,8,15],databas:14,date:[2,3,6],date_join:[3,6],datetimefield:6,deal:[15,18],deal_set:3,decimalfield:[6,15,18],declared_field:[3,8,15],declin:3,decline_appoint:15,defer:[3,15],defin:[3,15],deleg:[3,15],delet:14,delete_item:15,delete_menu_opt:15,delete_portfoliohaircut:15,denied_reason:[3,6],depend:[6,18],deploy:0,descript:[2,15,18],descriptor:[3,15],develop:2,django:[0,1,2,3,5,6,8,10,15,17,18],djangoproject:0,doc:0,doesnotexist:[3,15],dynam:[3,15],edit_menu_opt:15,edit_portfoliohaircut:15,email:[2,3,6],emailfield:[3,6],emailphonenumberorusernamemodelbackend:3,empti:2,empty_permit:[3,8,15],enforce_csrf:2,error_class:[3,8,15],errorlist:[3,8,15],exampl:[0,3,15],except:[3,15],execut:[3,15],expos:0,extra_kwarg:2,fals:[3,5,6,8,10,15,17],field:[2,3,6,8,15,18],fieldfil:[3,15],file:[0,3,6,8,15,18],filefield:[6,18],first:[3,15,17],first_nam:[2,3,6],foreignkei:[3,6,15,18],form:12,forward:[3,15],forwardmanytoonedescriptor:[3,15],from:[0,3,15],full:0,gener:0,genericviewset:2,get:[3,15],get_next_by_d:3,get_next_by_date_join:3,get_next_by_tim:3,get_previous_by_d:3,get_previous_by_date_join:3,get_previous_by_tim:3,get_queryset:2,get_status_displai:3,get_us:3,girl:2,global:5,global_const:[3,12],globalmenu:[2,3,6],globalmenuseri:2,globalmenuviewset:2,gmail:2,group:[3,6],hair_typ:[3,6],haircut:[2,17],haircutviewset:2,handl:[5,10,17],has_object_permiss:2,has_permiss:2,hello:[3,15],help:[5,10,17],hidden_hair_typ:[3,6],home:[0,3],home_login:3,home_safeti:3,home_styl:3,home_stylist:3,howto:0,http:0,hyperlinkedmodelseri:2,id_:[3,8,15],implement:[3,15],includ:0,index:12,inform:0,initi:[3,6,8,15,18],instanc:[2,3,8,15],integerfield:6,interview_tim:[3,6],is_act:[3,6],is_custom:11,is_staff:[3,6],is_stylist:[2,3,6],is_superus:[3,6],is_valid:3,iscurrentuserorsuperus:2,isownerofappoint:2,isownerofhaircut:2,isuserloggedin:2,item_custom:[3,6],item_menu:[3,6],item_menu_id:3,item_portfolio:[3,6,15],item_portfolio_id:3,iteminbil:[3,6],iteminbill_set:3,kwarg:[2,3],label_suffix:[3,8,15],last_login:[3,6],last_nam:[2,3,6],level:0,like:[3,15],list:0,listmodelmixin:2,load:[3,15],locat:[2,3,6,8],logentry_set:3,login:7,logout:3,manag:[3,6,8,12,15],mani:[3,15],manytomanydescriptor:3,manytomanyfield:[3,6],media:[3,8,15],menu:5,menu_opt:[15,18],menu_option_id:15,menuoptionform:15,meta:[2,3,8,15],migrat:[3,12,14,15],mixin:2,model:[6,12,18],model_nam:6,modelform:[3,8,15],modelviewset:2,modified_glob:[2,3,6],modified_global_id:3,modul:12,more:0,morearg:3,morekwarg:3,most:[3,15],multipleobjectsreturn:[3,15],my_app:0,myapp:[3,15],mymodel:[3,15],name:[0,1,2,3,6,8,15,18],need:17,newappointmentform:8,newportfoliohaircutform:15,newuserform:3,no_color:[5,10,17],none:[2,3,5,8,10,15,17],obj:2,object:[2,3,6,7,8,11,15,19],objectdoesnotexist:[3,15],obtain_selected_haircut:8,obtain_selected_menuopt:8,obtain_stylist_profil:8,old:14,one:[3,15],onlysuperuserscanmodifi:2,open:[3,15],oper:[6,18],option:[5,6,10,17],ordereddict:[3,8,15],org:2,other_app:0,owner:3,packag:12,page:12,parent:[3,15],password1:3,password2:3,password:[2,3,6],path:[3,15],pend:3,perform_cr:2,permiss:12,permission_class:2,phone_numb:[2,3,6],phone_regex:3,pictur:[2,15,18],pizza:3,pleas:0,portfolio:15,portfoliohaircut:[2,15,18],portfoliohaircut_set:3,portfoliohaircutseri:2,prefix:[3,8,15],price:[2,3,6,15,18],price_modifi:15,profil:[1,8,15],profile_pictur:[2,3,6],profile_r:8,profile_test:15,project:0,queri:[3,15],queryset:2,question:[3,6],questionnair:[3,6],questionnaire_id:3,read:[3,15],reason:[3,6,8],redirect_to_dashboard:7,ref:0,regexvalid:3,reinstate_appl:1,reject_applic:1,relat:[3,6,15,18],related_nam:[3,15],remove_menu_opt:15,render_application_statu:11,render_dashboard:11,request:[1,2,3,7,8,11,15],required_field:3,reschedule_appoint:[8,15],rescheduled_bycustom:3,rescheduled_bystylist:3,respons:[3,6],rest_framework:2,retrieve_appl:11,retrieve_us:7,retrievemodelmixin:2,returning_us:3,revers:[3,15],reversemanytoonedescriptor:[3,15],review:[3,6,7],rout:0,schedule_interview:1,search:12,search_real:8,see:0,select_menu_opt:15,self:2,serial:12,serializer_class:2,sessionauthent:2,set:12,settings_r:8,setup:12,side:[3,15],size:[3,15],sourc:[1,2,3,5,6,7,8,10,11,15,17,18,19],startproject:0,statu:[2,3,6],status_accept:3,status_choic:3,status_complet:3,status_declin:3,status_pend:3,status_recheduled_bystylist:3,status_rescheduled_bycustom:3,stderr:[5,10,17],stdout:[5,10,17],stuff:[3,15],stylist:[2,3,6,12,14],stylist_id:[3,15],stylist_r:[2,3,6],stylist_search:[2,8],stylistapplicationform:8,stylistconfig:15,stylistmenu:[2,3,6,15],stylistmenuseri:2,stylistmenuviewset:2,stylistseri:2,stylistviewset:2,submit_review:[8,15],submodul:[4,9,12,16],subpackag:12,suffix:2,test:12,textfield:[6,18],thi:[0,3,15],three:2,time:[3,6,15],top:3,topic:0,transact:15,two:2,update_averag:7,update_basic_inform:3,update_pric:19,upload_haircut:15,upload_pictur:[3,7],url:12,urlconf:0,urlpattern:0,use_required_attribut:[3,8,15],user:[2,3,6,7],user_id:3,user_login:2,user_logout:2,user_permiss:[3,6],usercreationform:3,userinform:3,userlog:7,usermanag:6,usernam:[3,6],username_field:3,userseri:2,userviewset:2,using:0,util:[3,8,12,15],valid:3,validated_data:2,valu:[0,3,15],variabl:0,verbose_nam:6,verbose_name_plur:6,view:[0,12],view_bil:[8,15],view_interview:1,view_log:[3,8,12,15],view_reject:1,view_stylist:1,view_stylist_appl:1,viewset:2,when:[3,15],world:[3,15],wrapper:[3,15],write_onli:2,wsgi:12,you:[3,15,17]},titles:["Clipper_V_0 package","administration package","api package","core package","core.management package","core.management.commands package","core.migrations package","core.utils package","customer package","customer.management package","customer.management.commands package","customer.utils package","Welcome to Clippr&#8217;s documentation!","manage module","setup module","stylist package","stylist.management package","stylist.management.commands package","stylist.migrations package","stylist.utils package"],titleterms:{"0001_initi":[6,18],"0002_auto_20170316_0030":6,admin:[1,2,3,8,15],administr:1,api:2,app:[1,2,3,8,15],backend:[2,3],clipper_v_0:0,clippr:12,command:[5,10,17],content:[0,1,2,3,4,5,6,7,8,9,10,11,15,16,17,18,19],core:[3,4,5,6,7],createdefaultappoint:10,createdefaulthaircut:17,createdefaultus:5,createglobalmenuopt:5,custom:[8,9,10,11],document:12,form:[3,8,15],global_const:7,indic:12,manag:[4,5,9,10,13,16,17],migrat:[6,18],model:[1,2,3,8,15],modul:[0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19],packag:[0,1,2,3,4,5,6,7,8,9,10,11,15,16,17,18,19],permiss:2,serial:2,set:0,setup:14,stylist:[15,16,17,18,19],submodul:[0,1,2,3,5,6,7,8,10,11,15,17,18,19],subpackag:[1,2,3,4,8,9,15,16],tabl:12,test:[1,2,3,8,15],url:[0,1,2,3,8,15],util:[7,11,19],view:[1,2,3,8,15],view_log:[7,11,19],welcom:12,wsgi:0}})