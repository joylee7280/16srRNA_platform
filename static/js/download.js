$(document).ready(function () {
    $('#dl').click(function (e) {
        e.preventDefault
        //ajax上傳文件必須通過FormData對象傳輸數據
        // var formdata = new FormData();
        // var user_proj = $('#select_proj').val();
        // formdata.append('user_proj', user_proj);
        $.ajax({
            url: "/ancom/ancom-subject/download/",
            type: 'post',
            // data: formdata,
            processData: false,//不處理數據
            contentType: false,//不設置內容類型，按原格式傳輸
            success: function (response) {
                // alert("success")
                window.open("/ancom/ancom-subject/download/")
                // window.close("/ancom/ancom-subject/download/")
            },
            error: function () {

                alert("失敗")
            }
        })
    })
})
