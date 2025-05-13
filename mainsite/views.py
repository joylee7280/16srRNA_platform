from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse,StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from mainsite.script import vis_ancombc,vis_ancom,vis_lefse_convert, vis_lefse,vis_lefse_output
import subprocess as sp
import json
import uuid
import os
import pandas as pd
import mimetypes
def index(request):
    request.session.clear()
    # print(request.session)
    return render(request, "index.html", locals())
def home(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]

    return render(request, "home.html", locals())
def login(request):
    # request.session.clear()
    if request.method == "POST":
        ur_email = request.POST['user_email']
        s_userID = str(uuid.uuid5(uuid.NAMESPACE_DNS, ur_email))
        print(s_userID)
        sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID], shell=True,
                       capture_output=True, text=True) #創建使用者資料夾
        sp.run(["mkdir /work1791/b09901010/project/mainsite/templates/user_output/"+s_userID], shell=True,
                                        capture_output=True, text=True)
    else:
        pass
    try:
        # if ur_email:request.session['ur_email'] = ur_email
        if s_userID:
            request.session['s_userID'] = s_userID
        return render(request, "home.html", locals())
    except:
        pass
        return render(request, "login.html", locals())
def handle_uploaded_file(file,s_uploadPath):
    with open(s_uploadPath+"%s" % file, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
@csrf_exempt
def addproj(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
    if "user_proj" in request.POST.keys():
        ur_proj = request.POST["user_proj"]
        print("ur_proj:"+ur_proj)
    if request.method == "POST":
        print(request.POST.keys())
        if "user_proj" in request.POST.keys():
            if "sample-metadata_name" not in request.POST.keys():
                if "table_name" not in request.POST.keys():
                    if "taxonomy_name" not in request.POST.keys():
                        print("2")
                        if os.path.exists("/work1791/b09901010/project/user_folder/"+s_userID+"/"+request.POST["user_proj"]):
                            print("exist")
                            return HttpResponse("Project已存在:"+request.POST["user_proj"])
                        else:
                            ur_proj = request.POST['user_proj']
                            sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj], shell=True,
                                        capture_output=True, text=True)
                            sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input"], shell=True,
                                        capture_output=True, text=True)
                            sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/metadata/"], shell=True,
                                        capture_output=True, text=True)
                            sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/table/"], shell=True,
                                        capture_output=True, text=True)
                            sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/taxonomy/"], shell=True,
                                        capture_output=True, text=True)
                            sp.run(["mkdir /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/output"], shell=True,
                                        capture_output=True, text=True)
                            sp.run(["mkdir /work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj], shell=True,
                                        capture_output=True, text=True)
                            ################ log ################
                            sp.run(["touch /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/project.txt"], shell=True,
                                                                capture_output=True, text=True)
                            path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/project.txt"
                            with open(path, 'a') as f:
                                f.write("Project data\n")
                                f.write("# name:"+ur_proj+"\n")
                                f.write("\n")
                                f.write("Analysis progress:\n")
                            #####################################
                            return HttpResponse('Project已建立:'+request.POST["user_proj"])
        if "sample-metadata" in request.FILES.keys():
            print("3")
            print(request.POST)
            ur_proj = request.POST['projName_2']
            file_obj = request.FILES.get('sample-metadata')
            print(ur_proj)
            file_name = file_obj.name
            print('>>>>',file_name)
            with open("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/metadata/"+file_name, 'wb')as f:
                for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                    f.write(chunk)
            return HttpResponse(file_name+'已上傳')

        if "table" in request.FILES.keys():
            print("4")
            print(request.POST)
            ur_proj = request.POST['projName_2']
            file_obj = request.FILES.get('table')
            print(ur_proj)
            file_name = file_obj.name
            print('>>>>',file_name)
            with open("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/table/"+file_name, 'wb')as f:
                for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                    f.write(chunk)
            return HttpResponse(file_name+'已上傳')

        if "taxonomy" in request.FILES.keys():
            print("5")
            print(request.POST)
            ur_proj = request.POST['projName_2']
            file_obj = request.FILES.get('taxonomy')
            print(ur_proj)
            file_name = file_obj.name
            print('>>>>',file_name)
            with open("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/taxonomy/"+file_name, 'wb')as f:
                for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                    f.write(chunk)
            return HttpResponse(file_name+'已上傳')
    return render(request, "addproj.html", locals())
@csrf_exempt
def ancom(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        path = "/work1791/b09901010/project/user_folder/"+s_userID
        proj_list = os.listdir(path)
        # return HttpResponse(proj_list)
    if request.method == "POST":
        if "user_proj" in request.POST.keys() and "target_file" not in request.POST.keys():
            ur_proj = request.POST['user_proj']
            if ur_proj:
                request.session['ur_proj'] = ur_proj
            path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/"
            metadata_list = os.listdir(path)
            metadata_list_as_json = json.dumps(metadata_list)
            print(metadata_list)
            path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/table/"
            table_list = os.listdir(path)
            table_list_as_json = json.dumps(table_list)
            path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/taxonomy/"
            taxonomy_list = os.listdir(path)
            all=[metadata_list,table_list,taxonomy_list]
            all_list_as_json = json.dumps(all)
            return HttpResponse(all_list_as_json,'application/json')
        if "target_file" in request.POST.keys() and "target_clas" not in request.POST.keys():
            ur_proj = request.POST['user_proj']
            metadata = request.POST['target_metadata']
            table = request.POST['target_table']
            taxonomy = request.POST['target_taxonomy']
            sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/"+metadata,sep="\t",header=0)
            class_list=[]
            # print(sample)
            for row in sample:
                class_list.append(row)
            # print(class_list)
            class_list_as_json = json.dumps(class_list)
            return HttpResponse(class_list_as_json,'application/json') #要加後面的!
        if "target_clas" in request.POST.keys() and "target_para" not in request.POST.keys():
            print("dddddddddddddddddddddd")
            ur_proj = request.POST['user_proj']
            metadata = request.POST['target_metadata']
            sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/"+metadata,sep="\t",header=0)
            target_clas = request.POST['target_clas']
            para_list_bf = sample[target_clas]
            para_list = para_list_bf.tolist()
            print(para_list)
            para_list_as_json = json.dumps(para_list)
            # print(target_clas)
            # print("heeeeeeeeeeee")
            return HttpResponse(para_list_as_json,'application/json')
        if "target_para" in request.POST.keys() and "target_meta" not in request.POST.keys():
            print("*********************************")
            ur_proj = request.POST['user_proj']
            target_para = request.POST['target_para']
            print(target_para)
            sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/"+metadata,sep="\t",header=0)
            meta_list=[]
            for i in sample:
                meta_list.append(i)
            # print(type(meta_list))
            meta_list_as_json = json.dumps(meta_list)
            # print(type(meta_list_as_json))
            return HttpResponse(meta_list_as_json,'application/json') #要加後面的!
        if "target_meta" in request.POST.keys():
            ur_proj = request.POST['user_proj']
            target_clas = request.POST['target_clas']
            target_para = request.POST['target_para']
            target_meta = request.POST['target_meta']
            print(target_meta)
            vis_ancom(s_userID,ur_proj,target_metadata,target_table,target_taxonomy,target_clas,target_para,target_meta)
            return HttpResponse("ancom執行完")
    return render(request, "ancom.html", locals())
# def ancom(request):
#     if "s_userID" in request.session:
#         s_userID = request.session["s_userID"]
#         path = "/work1791/b09901010/project/user_folder/"+s_userID
#         proj_list = os.listdir(path)
#         # return HttpResponse(proj_list)
#     if request.method == "POST":
#         if "user_proj" in request.POST.keys() and "target_clas" not in request.POST.keys():
#             ur_proj = request.POST['user_proj']
#             if ur_proj:
#                 request.session['ur_proj'] = ur_proj
#             sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/sample-metadata.tsv",sep="\t",header=0)
#             class_list=[]
#             for row in sample:
#                 class_list.append(row)
#             print(class_list)
#             class_list_as_json = json.dumps(class_list)
#             return HttpResponse(class_list_as_json,'application/json') #要加後面的!
#         if "target_clas" in request.POST.keys() and "target_para" not in request.POST.keys():
#             ur_proj = request.POST['user_proj']
#             sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/sample-metadata.tsv",sep="\t",header=0)
#             target_clas = request.POST['target_clas']
#             para_list_bf = sample[target_clas]
#             para_list = para_list_bf.tolist()
#             print(para_list)
#             para_list_as_json = json.dumps(para_list)
#             print(target_clas)
#             return HttpResponse(para_list_as_json,'application/json')
#         if "target_para" in request.POST.keys() and "target_meta" not in request.POST.keys():
#             print("*********************************")
#             ur_proj = request.POST['user_proj']
#             target_para = request.POST['target_para']
#             print(target_para)
#             sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/sample-metadata.tsv",sep="\t",header=0)
#             meta_list=[]
#             for i in sample:
#                 meta_list.append(i)
#             # print(type(meta_list))
#             meta_list_as_json = json.dumps(meta_list)
#             # print(type(meta_list_as_json))
#             return HttpResponse(meta_list_as_json,'application/json') #要加後面的!
#         if "target_meta" in request.POST.keys():
#             ur_proj = request.POST['user_proj']
#             target_clas = request.POST['target_clas']
#             target_para = request.POST['target_para']
#             target_meta = request.POST['target_meta']
#             print(target_meta)
#             vis_ancom(s_userID,ur_proj,target_clas,target_para,target_meta)
#             return HttpResponse("ancom執行完")
#     return render(request, "ancom.html", locals())
@csrf_exempt
def ancombc(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        path = "/work1791/b09901010/project/user_folder/"+s_userID
        proj_list = os.listdir(path)
        print(proj_list)
        # return HttpResponse(proj_list)
    if request.method == "POST":
        if "user_proj" in request.POST.keys() and "target_clas" not in request.POST.keys():
            ur_proj = request.POST['user_proj']
            if ur_proj:
                request.session['ur_proj'] = ur_proj
            sample = pd.read_csv("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/"+"input/metadata/sample-metadata.tsv",sep="\t",header=0)
            class_list=[]
            for row in sample:
                class_list.append(row)
            print(class_list)
            class_list_as_json = json.dumps(class_list)
            return HttpResponse(class_list_as_json,'application/json') #要加後面的!
        if "target_clas" in request.POST.keys():
            ur_proj = request.POST['user_proj']
            target_clas = request.POST['target_clas']
            print(target_clas)
            vis_ancombc(s_userID,ur_proj,target_clas)
            return HttpResponse("ancombc執行完")
    return render(request, "ancombc.html", locals())
@csrf_exempt
def lefse(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        path = "/work1791/b09901010/project/user_folder/"+s_userID
        proj_list = os.listdir(path)
        print(proj_list)
        # return HttpResponse(proj_list)
    if request.method == "POST":
        if "user_proj" in request.POST.keys():
            ur_proj = request.POST['user_proj']
            if ur_proj:
                request.session['ur_proj'] = ur_proj
                print(ur_proj)
            vis_lefse_convert(s_userID,ur_proj)
            vis_lefse(s_userID,ur_proj)
            sp.run(["cp /work1791/b09901010/project/mainsite/templates/lefse_output.html /work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/LEfSe/"], shell=True,
                                        capture_output=True, text=True)
            vis_lefse_output(s_userID,ur_proj)
    return render(request, "lefse.html", locals())

@csrf_exempt
def manageproj(request):
    if "s_userID" in request.session:
        print("yes")
        s_userID = request.session["s_userID"]
        print(s_userID)
        path = "/work1791/b09901010/project/user_folder/"+s_userID
        proj_list = os.listdir(path)
        # return HttpResponse(proj_list)
    if request.method == "POST":
        if "user_proj" in request.POST.keys():
            ur_proj = request.POST['user_proj']
            if ur_proj:
                request.session['ur_proj'] = ur_proj
        if "operation" in request.POST.keys():
            operation = request.POST['operation']
            print(operation)
            ### operation = "add" ###
            if operation == "add" and "sample-metadata" in request.FILES.keys():
                print(request.FILES.keys())
                ur_proj = request.POST['projName_2']
                file_obj = request.FILES.get('sample-metadata')
                file_name = file_obj.name
                print('>>>>',file_name)
                with open("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/metadata/"+file_name, 'wb')as f:
                    for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                        f.write(chunk)
            if operation == "add" and "table" in request.FILES.keys():
                ur_proj = request.POST['projName_2']
                file_obj = request.FILES.get('table')
                file_name = file_obj.name
                print('>>>>',file_name)
                with open("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/table/"+file_name, 'wb')as f:
                    for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                        f.write(chunk)
            if operation == "add" and "taxonomy" in request.FILES.keys():
                ur_proj = request.POST['projName_2']
                file_obj = request.FILES.get('taxonomy')
                file_name = file_obj.name
                print('>>>>',file_name)
                with open("/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/taxonomy/"+file_name, 'wb')as f:
                    for chunk in file_obj.chunks():#chunks()每次读取数据默认我64k
                        f.write(chunk)
            if operation == "remove_data" and request.POST['filetype']=="table":
                path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/table/"
                if 'buttontype' in request.POST.keys():
                    if request.POST['buttontype']=="table":
                        rm_file = request.POST.getlist('tableForm')
                        for i in rm_file:
                            sp.run(["rm -rf "+path+i], shell=True,capture_output=True, text=True)
                        table = os.listdir(path)
                        return JsonResponse(table,safe=False)
                else:
                    print(request.POST)
                    table = os.listdir(path)
                    print(table)
                    return JsonResponse(table,safe=False)
            if operation == "remove_data" and request.POST['filetype']=="sample":
                path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/metadata/"
                if 'buttontype' in request.POST.keys():
                    if request.POST['buttontype']=="sample":
                        rm_file = request.POST.getlist('sampleForm')
                        for i in rm_file:
                            sp.run(["rm -rf "+path+i], shell=True,capture_output=True, text=True)
                        metadata = os.listdir(path)
                        return JsonResponse(metadata,safe=False)
                else:
                    print(request.POST)
                    metadata = os.listdir(path)
                    return JsonResponse(metadata,safe=False)

            if operation == "remove_data" and request.POST['filetype']=="taxonomy":
                path = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/taxonomy/"
                if 'buttontype' in request.POST.keys():
                    if request.POST['buttontype']=="taxonomy":
                        rm_file = request.POST.getlist('taxonomyForm')
                        for i in rm_file:
                            sp.run(["rm -rf "+path+i], shell=True,capture_output=True, text=True)
                        taxonomy = os.listdir(path)
                        return JsonResponse(taxonomy,safe=False)
                else:
                    print(request.POST)
                    taxonomy = os.listdir(path)
                    print(taxonomy)
                    return JsonResponse(taxonomy,safe=False)
            # if operation == "remove_data_chosen":
            #     a=request.POST.getist("sample")
                # if request.POST['r_table'] == "true":
                #     print("remove_table")
                #     sp.run(["rm /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/table/table.qza"], shell=True,
                #                         capture_output=True, text=True)
                # if request.POST['r_taxonomy'] == "true":
                #     print("remove_taxonomy")
                #     sp.run(["rm /work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj+"/input/taxonomy/taxonomy.qza"], shell=True,
                #                         capture_output=True, text=True)
            ### operation = "download" ###
            if operation == "download":
                result = {"ancom":"false",
                          "ancombc":"false",
                          "lefse":"false"}
                path = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj
                # ancom #
                if os.path.isdir(path+"/ancom/"):
                    if len(os.listdir(path+"/ancom/")) != 0:
                        sp.run(["tar -zcvf "+path+"ancom.gz "+path+"ancom_unzip"], shell=True,
                        capture_output=True, text=True)
                        result["ancom"] = "true"
                # ancombc #
                if os.path.isdir(path+"/ancombc/"):
                    if len(os.listdir(path+"/ancombc/")) != 0:
                        sp.run(["tar -zcvf "+path+"ancombc.gz "+path+"ancombc"], shell=True,
                        capture_output=True, text=True)
                        result["ancombc"] = "true"
                # lefse #
                if os.path.isdir(path+"/LEfSe/"):
                    if len(os.listdir(path+"/LEfSe/")) != 0:
                        sp.run(["tar -zcvf "+path+"LEfSe.gz "+path+"LEfSe"], shell=True,
                        capture_output=True, text=True)
                        result['lefse']='true'
                return JsonResponse(result,safe=False)
            if operation == "remove_proj":
                print("here")
                print(s_userID)
                print(ur_proj)
                path_file = "/work1791/b09901010/project/user_folder/"+s_userID+"/"+ur_proj
                sp.run(["rm -rf "+path_file+"/*"], shell=True,
                                        capture_output=True, text=True)
                sp.run(["rmdir "+path_file], shell=True,
                                        capture_output=True, text=True)
                path_file = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj
                sp.run(["rm -rf "+path_file+"/*"], shell=True,
                                        capture_output=True, text=True)
                sp.run(["rmdir "+path_file], shell=True,
                                        capture_output=True, text=True)
                path_file = "/work1791/b09901010/project/mainsite/static/user_output/"+s_userID+"/"+ur_proj
                sp.run(["rm -rf "+path_file+"/*"], shell=True,
                                        capture_output=True, text=True)
                sp.run(["rmdir "+path_file], shell=True,
                                        capture_output=True, text=True)
                print(path_file)
                return render(request, "manageproj.html", locals())
            # return HttpResponse(class_list_as_json,'application/json') #要加後面的!
    return render(request, "manageproj.html", locals())
############ Manageproj download project ############
@csrf_exempt
def download_ancomzip(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filename = "ancom.gz"
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/ancom/"+filename
    file = open(filepath,'rb')
    response = FileResponse(file)
    response['Content-Tyep']='application/octet-stream'
    return response
@csrf_exempt
def download_ancombczip(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/ancombc/ancombc.gz"
    print(filepath)
    file = open(filepath,'rb')
    response = FileResponse(file)
    response['Content-Tyep']='application/octet-stream'
    return response
@csrf_exempt
def download_lefsezip(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/LEfSe/LEfSe.gz"
    print(filepath)
    file = open(filepath,'rb')
    response = FileResponse(file)
    response['Content-Tyep']='application/octet-stream'
    return response

############ View ############
@csrf_exempt
def view_ancom(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    return render(request,"user_output/"+s_userID+"/"+ur_proj+"/ancom/ancom_unzip/index.html",locals())
#ancombc:data
@csrf_exempt
def view_ancombc_d(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    return render(request,"user_output/"+s_userID+"/"+ur_proj+"/ancombc/differentials_unzip/index.html",locals())
#ancombc:barplot
@csrf_exempt
def view_ancombc_b(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    return render(request,"user_output/"+s_userID+"/"+ur_proj+"/ancombc/differentials_barplot_unzip/index.html",locals())
@csrf_exempt
def view_ancombc_barplot(request,item):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    ur = "user_output/"+s_userID+"/"+ur_proj+"/ancombc/differentials_barplot_unzip/{}".format(item)
    return render(request,ur,locals())
#lefse:barplot
@csrf_exempt
def view_lefse_output(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    return render(request,"/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/LEfSe/lefse_output.html",locals())
#lefse:barplot
@csrf_exempt
def view_lefse_b(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filename = "lefse_final_lda.pdf"
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/LEfSe/"+filename
    path = open(filepath,'r')
    response = FileResponse(open(filepath, 'rb'))
    response['content_type'] = "application/octet-stream"
    # mime_type, _ = mimetypes.guess_type(filepath)
    # response = HttpResponse(path, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
#lefse:cladogram
@csrf_exempt
def view_lefse_c(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filename = "lefse_total_clado.pdf"
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/LEfSe/"+filename
    path = open(filepath,'r')
    response = FileResponse(open(filepath, 'rb'))
    response['content_type'] = "application/octet-stream"
    # mime_type, _ = mimetypes.guess_type(filepath)
    # response = HttpResponse(path, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

############ Ancom download ############
#ancom:data.tsv
@csrf_exempt
def download_data(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filename = "data.tsv"
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/ancom/ancom_unzip/"+filename
    path = open(filepath,'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
#ancom:ancom.tsv
@csrf_exempt
def download_ancom(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filename = "ancom.tsv"
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/ancom/ancom_unzip/"+filename
    path = open(filepath,'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
#ancom:percentage_abundance.tsv
@csrf_exempt
def download_abun(request):
    if "s_userID" in request.session:
        s_userID = request.session["s_userID"]
        print(s_userID)
    if "ur_proj" in request.session:
        ur_proj = request.session["ur_proj"]
    filename = "percent-abundances.tsv"
    filepath = "/work1791/b09901010/project/mainsite/templates/user_output/"+s_userID+"/"+ur_proj+"/ancom/ancom_unzip/"+filename
    path = open(filepath,'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type = mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def image(request):
    # if "s_userID" in request.session:
    #     s_userID = request.session["s_userID"]
    #     print(s_userID)
    # if "ur_proj" in request.session:
    #     ur_proj = request.session["ur_proj"]
    s_userID = "19fc23c5-ec94-5299-b0ef-02de1cd5d6be"
    ur_proj = "pro1"
    image_data = open("/work1791/b09901010/project/mainsite/static/user_output/"+s_userID+"/"+ur_proj+"/LEfSe/lefse_final_lda.png","rb").read()
    return HttpResponse(image_data)



