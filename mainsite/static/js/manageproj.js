$(function () {

    $('#target_proj').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        $("#radios").css("display", "inline"); // 顯示第二層選單
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {

            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })

    $('#radio1').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', "add");
        $("#add").css("display", "inline")
        $("#remove").css("display", "none")
        $("#download").css("display", "none")
        $("#remove_proj").css("display", "none")
        $("#remove_file").css("display", "none")
        $("#select_file").css("display", "none")
        $("#sample_blk").css("display", "none")
        $("#table_blk").css("display", "none")
        $("#taxonomy_blk").css("display", "none")
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // $.each(response, function (key, value) {
                //     // alert("測試")
                //     $('#select_clas').append('<option>' + response[key] + '</option>')
                // });
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })

    $('#radio2').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', "remove_data");
        formdata.append('filetype', "none");
        $("#add").css("display", "none")
        $("#remove_file").css("display", "inline")
        $("#download").css("display", "none")
        $("#remove_proj").css("display", "none")

        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert(response)
                //////////////////////////////////
                if (response["sample"] == 'true') {
                    $("#r_sample_div").css("display", "inline")
                    $("#r_sample").css("display", "inline")
                }
                if (response["table"] == 'true') {
                    $("#r_table_div").css("display", "inline")
                    $("#r_table").css("display", "inline")
                }
                if (response["taxonomy"] == 'true') {
                    $("#r_taxonomy_div").css("display", "inline")
                    $("#r_taxonomy").css("display", "inline")
                }

            },
            error: function () {
                // alert("失敗")
            }
        })
        // alert("success")
    })

    $('#deter_sample').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', "remove_data");
        formdata.append('filetype', "sample");
        $("#add").css("display", "none")
        $("#remove_file").css("display", "inline")
        $("#select_file").css("display", "inline")
        $("#download").css("display", "none")
        $("#remove_proj").css("display", "none")
        $("#sample_blk").css("display", "inline")
        $("#table_blk").css("display", "none")
        $("#taxonomy_blk").css("display", "none")

        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert(response)
                s_html = ""
                $.each(response, function (key, value) {
                    s_html += "<label><input type='checkbox' name='sampleForm' " + "value=" + response[key] + ">" + response[key] + "</label><br>";
                })
                $("#sample_opt").html(s_html)
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })
    //// button remove sample file ////
    $('#rmB_sample').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        // formdata.append('user_proj', user_proj);
        // formdata.append('operation', "remove_data");
        // formdata.append('filetype', "sample");
        // formdata.append('buttontype', "sample");
        request = $("#sampleForm").serialize() + "&user_proj=" + user_proj + "&operation=remove_data" + "&filetype=sample" + "&buttontype=sample";
        $.post("/manageproj/", request, function (response) {
            s_html = ""
            $.each(response, function (key, value) {
                s_html += "<label><input type='checkbox' name='sampleForm' " + "value=" + response[key] + ">" + response[key] + "</label><br>";
            })
            $("#sample_opt").html(s_html)
        })
        // $.ajax({
        //     url: "/manageproj/",
        //     type: 'post',
        //     data: formdata + $("#sampleForm").serializeObject(),
        //     processData: false,//不處理數據
        //     contentType: false,//不設置內容類型，按原格式傳輸
        //     success: function (response) {
        //         // alert("test")
        //     },
        //     error: function () {
        //         alert("失敗")
        //     }
        // })
        // alert("success")
    })
    $('#deter_table').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', "remove_data");
        formdata.append('filetype', "table");
        $("#add").css("display", "none")
        $("#remove_file").css("display", "inline")
        $("#select_file").css("display", "inline")
        $("#download").css("display", "none")
        $("#remove_proj").css("display", "none")
        $("#sample_blk").css("display", "none")
        $("#table_blk").css("display", "inline")
        $("#taxonomy_blk").css("display", "none")

        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                s_html = ""
                $.each(response, function (key, value) {
                    s_html += "<label><input type='checkbox' name='tableForm' " + "value=" + response[key] + ">" + response[key] + "</label><br>";
                })
                $("#table_opt").html(s_html)
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })
    //// button remove table file ////
    $('#rmB_table').click(function (e) {
        e.preventDefault
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        request = $("#tableForm").serialize() + "&user_proj=" + user_proj + "&operation=remove_data" + "&filetype=table" + "&buttontype=table";
        $.post("/manageproj/", request, function (response) {
            s_html = ""
            $.each(response, function (key, value) {
                s_html += "<label><input type='checkbox' name='tableForm' " + "value=" + response[key] + ">" + response[key] + "</label><br>";
            })
            $("#table_opt").html(s_html)
        })

    })
    $('#deter_taxonomy').click(function (e) {

        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', "remove_data");
        formdata.append('filetype', "taxonomy");
        $("#add").css("display", "none")
        $("#remove_file").css("display", "inline")
        $("#select_file").css("display", "inline")
        $("#download").css("display", "none")
        $("#remove_proj").css("display", "none")
        $("#sample_blk").css("display", "none")
        $("#table_blk").css("display", "none")
        $("#taxonomy_blk").css("display", "inline")
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert(typeof (response))
                s_html = ""
                $.each(response, function (key, value) {
                    s_html += "<label><input type='checkbox' name='taxonomyForm' " + "value=" + response[key] + ">" + response[key] + "</label><br>";
                })
                $("#taxonomy_opt").html(s_html)
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })
    //// button remove taxonomy file ////
    $('#rmB_taxonomy').click(function (e) {

        e.preventDefault
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        request = $("#taxonomyForm").serialize() + "&user_proj=" + user_proj + "&operation=remove_data" + "&filetype=taxonomy" + "&buttontype=taxonomy";
        $.post("/manageproj/", request, function (response) {
            s_html = ""
            $.each(response, function (key, value) {
                s_html += "<label><input type='checkbox' name='taxonomyForm'" + "value=" + response[key] + ">" + response[key] + "</label><br>";
            })
            $("#taxonomy_opt").html(s_html)
        })

    })
    // $('#remove_file_confirm').click(function (e) {
    //     e.preventDefault
    //     //ajax上傳文件必須通過FormData對象傳輸數據
    //     var formdata = new FormData();
    //     var user_proj = $('#select_proj').val();
    //     // alert($('#select_proj').val())
    //     formdata.append('user_proj', user_proj);
    //     formdata.append('operation', "remove_data_chosen");
    //     $("#add").css("display", "none")
    //     $("#remove_file").css("display", "inline")
    //     $("#download").css("display", "none")
    //     $("#remove_proj").css("display", "none")
    //     //////////////////////////////////
    //     request = $("#fileForm").serialize() + "&user_proj=" + user_proj + "&operation=remove_data_chosen";
    //     $.post("/manageProject/", request, function (response) {

    //     })
    // $.ajax({
    //     url: "/manageproj/",
    //     type: 'post',
    //     data: formdata,
    //     processData: false,//不處理數據
    //     contentType: false,//不設置內容類型，按原格式傳輸
    //     success: function (response) {
    //         window.location.reload()
    //     },
    //     error: function () {
    //         alert("失敗")
    //     }
    // })
    // alert("success")
    // })
    $('#radio3').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', "download");
        $("#add").css("display", "none")
        $("#remove").css("display", "none")
        $("#download").css("display", "inline")
        $("#remove_proj").css("display", "none")
        $("#remove_file").css("display", "none")
        $("#select_file").css("display", "none")
        $("#sample_blk").css("display", "none")
        $("#table_blk").css("display", "none")
        $("#taxonomy_blk").css("display", "none")
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert(response["ancombc"])
                if (response["ancom"] == 'true') {
                    $("#download_ancom").css("display", "inline")
                }
                if (response["ancombc"] == 'true') {
                    $("#download_ancombc").css("display", "inline")
                }
                if (response["lefse"] == 'true') {
                    $("#download_lefse").css("display", "inline")
                }
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })

    $('#radio4').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        $("#add").css("display", "none")
        $("#remove").css("display", "none")
        $("#download").css("display", "none")
        $("#remove_proj").css("display", "inline")
        $("#remove_file").css("display", "none")
        $("#select_file").css("display", "none")
        $("#sample_blk").css("display", "none")
        $("#table_blk").css("display", "none")
        $("#taxonomy_blk").css("display", "none")
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {

            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })


    //// Remove files from project ////
    // $('#remove_file_confirm').click(function (e) {
    //     e.preventDefault
    //     //ajax上傳文件必須通過FormData對象傳輸數據
    //     var formdata = new FormData();
    //     var user_proj = $('#select_proj').val();
    //     // alert($('#select_proj').val())
    //     formdata.append('user_proj', user_proj);
    //     formdata.append('operation', "remove_data_chosen");
    //     $("#add").css("display", "none")
    //     $("#remove_file").css("display", "inline")
    //     $("#download").css("display", "none")
    //     $("#remove_proj").css("display", "none")
    //     //////////////////////////////////
    //     if ($('#r_sample').is(":checked")) {
    //         formdata.append('r_sample', "true");
    //     }
    //     else {
    //         formdata.append('r_sample', "false");
    //     }
    //     if ($('#r_table').is(":checked")) {
    //         formdata.append('r_table', "true");
    //     }
    //     else {
    //         formdata.append('r_table', "false");
    //     }
    //     if ($('#r_taxonomy').is(":checked")) {
    //         formdata.append('r_taxonomy', "true");
    //     }
    //     else {
    //         formdata.append('r_taxonomy', "false");
    //     }
    //     $.ajax({
    //         url: "/manageproj/",
    //         type: 'post',
    //         data: formdata,
    //         processData: false,//不處理數據
    //         contentType: false,//不設置內容類型，按原格式傳輸
    //         success: function (response) {
    //             // window.location.reload()
    //         },
    //         error: function () {
    //             alert("失敗")
    //         }
    //     })
    //     // alert("success")
    // })

    ///////////////////// remove project /////////////////////
    $('#remove_confirm').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        formdata.append('operation', 'remove_proj');
        alert("Are you sure you want to remove project?")
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                window.location.reload()
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })

    // $('#remove_files').click(function (e) {
    //     e.preventDefault
    //     //ajax上傳文件必須通過FormData對象傳輸數據
    //     var formdata = new FormData();
    //     var user_proj = $('#select_proj').val();
    //     // alert($('#select_proj').val())
    //     formdata.append('user_proj', user_proj);
    //     // formdata.append('option', "ancom");
    //     formdata.append('operation', 'remove_files');
    //     if (sample.checked) {
    //         alert("有勾選");
    //     } else {
    //         alert("沒有勾選");
    //     }
    //     $.ajax({
    //         url: "/manageproj/",
    //         type: 'post',
    //         data: formdata,
    //         processData: false,//不處理數據
    //         contentType: false,//不設置內容類型，按原格式傳輸
    //         success: function (response) {
    //             $('#file').append('<input type="button" id=' + response[key] + ' value="Remove">')
    //         },
    //         error: function () {
    //             alert("失敗")
    //         }
    //     })
    //     // alert("success")
    // })

    ///////////////////// upload sample /////////////////////
    $('#uploaded_sample').uploadFile({
        allowedTypes: "tsv,txt",
        url: "/manageproj/",
        fileName: "sample-metadata",
        showDelete: true,
        showDone: false,
        showProgress: true,
        dynamicFormData: function () {
            var nameVal = $('#select_proj').val();
            var uploadParam = {
                operation: "add",
                projName_2: nameVal

            }
            return uploadParam
        }, onSuccess: function (y, x, z, s) {
            filecount = filecount + 1
        }
    })
    ///////////////////// upload table /////////////////////
    $('#uploaded_table').uploadFile({
        allowedTypes: "qza",
        url: "/manageproj/",
        fileName: "table",
        showDelete: true,
        showDone: false,
        showProgress: true,
        dynamicFormData: function () {
            var nameVal = $('#select_proj').val();
            var uploadParam = {
                operation: "add",
                projName_2: nameVal

            }
            return uploadParam
        },
        onSuccess: function (y, x, z, s) {
            filecount = filecount + 1
        }
    })
    ///////////////////// upload taxonomy /////////////////////
    $('#uploaded_taxonomy').uploadFile({
        allowedTypes: "qza",
        url: "/manageproj/",
        fileName: "taxonomy",
        showDelete: true,
        showDone: false,
        showProgress: true,
        dynamicFormData: function () {
            var nameVal = $('#select_proj').val();
            var uploadParam = {
                projName_2: nameVal,
                operation: "add"
            }
            return uploadParam
        },
        onSuccess: function (y, x, z, s) {
            filecount = filecount + 1

        }

    }
    )
    //download
    $('#download_ancom').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        var formdata = new FormData();
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        // formdata.append('option', "ancom");
        formdata.append('operation', 'download_ancom');
        $.ajax({
            url: "/manageproj/",
            type: 'post',
            data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                $('#file').append('<input type="button" id=' + response[key] + ' value="Remove">')
            },
            error: function () {
                alert("失敗")
            }
        })
        // alert("success")
    })
    $('#view_b').click(function (e) {
        e.preventDefault
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        $.ajax({
            url: "/lefse/barplot/",
            type: 'post',
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert(response)

                window.open("/lefse/barplot/")
            },
            error: function () {
                alert("失敗")
            }
        })
    })
    $('#view_c').click(function (e) {
        e.preventDefault
        var user_proj = $('#select_proj').val();
        // alert($('#select_proj').val())
        formdata.append('user_proj', user_proj);
        //ajax上傳文件必須通過FormData對象傳輸數據
        $.ajax({
            url: "/lefse/cladogram/",
            type: 'post',
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert(response)
                window.open("/lefse/cladogram/")
            },
            error: function () {
                alert("失敗")
            }
        })
    })
})