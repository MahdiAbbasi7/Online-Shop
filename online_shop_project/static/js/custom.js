function sendArticleComment(articleId){
        var comment = $('#commentText').val();
        var parentID =  $('#parent_id').val();
    // ajax ==> asynchronous javascript and xml
    //json ==> javascript object notation
    $.get('/articles/add_article_comment',{
        comment,
        articleId,
        parentID
    }).then(res => {
        console.log(res);
        location.reload();
    }
    );
}

function filterProducts(){
    const filterPrice = $('#sl2').val();
    const start_price = filterPrice.split(',')[0];
    const end_price = filterPrice.split(',')[1];
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit();
}

function fillPage(page){
    $('#page').val(page);
    $('#filter_form').submit();

}

function fillParentID(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}

function addProductToOrder(productID){
    const productCount = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + productID + '$count=' + productCount).then(res =>{
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        })


        /*if (res.status === 'success') {
            Swal.fire({
                title: 'اعلان',
                text: "محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد",
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'باشه ممنون'
            });
        } else if (res.status === 'not_found') {
            Swal.fire({
                title: 'اعلان',
                text: "محصول مورد نظر یافت نشد",
                icon: 'error',
                show
                CancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'باشه ممنون'
            });
        }*/
    });
}


function removeOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


// detailID : for order detail id
// state : for increase of decrease number of product
function changeOrderDetail(detailId, state){
    $.get('/user/change-order-detail?detail_id=' + detailId + '&state='+ state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}