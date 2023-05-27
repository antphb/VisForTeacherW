function getCodes(tinhthanh, quanhuyen, phuongxa) {
    var maTinhThanh = "", maQuanHuyen = "", maPhuongXa = "";
    
    // gọi API và lấy danh sách tỉnh/thành phố
    $.getJSON("https://provinces.open-api.vn/api/?depth=3", function(data) {
        // tìm và lấy mã code của tỉnh/thành phố
        $.each(data, function(index, value) {
            if (value.name === tinhthanh) {
                // console.log(value.name);
                maTinhThanh = value.code;
                $("#TinhThanh").val(maTinhThanh).change();
                return false;
            }
        });

        // nếu không tìm thấy tỉnh/tp thì trả về null
        if (!maTinhThanh) {
            console.log("Không tìm thấy mã code cho tỉnh/thành phố " + tinhthanh);
            return null;
        }

        // gọi API và lấy danh sách quận/huyện theo mã code của tỉnh/thành phố đã tìm được
        $.getJSON("https://provinces.open-api.vn/api/p/" + maTinhThanh + "?depth=2", function(data) {
            // tìm và lấy mã code của quận/huyện
            $.each(data.districts, function(index, value) {
                if (value.name === quanhuyen) {
                    maQuanHuyen = value.code;
                    $("#QuanHuyen").val(maQuanHuyen).change();
                    return false;
                }
            });

            // nếu không tìm thấy quận/huyện thì trả về null
            if (!maQuanHuyen) {
                console.log("Không tìm thấy mã code cho quận/huyện " + quanhuyen);
                return null;
            }

            // gọi API và lấy danh sách phường/xã theo mã code của quận/huyện đã tìm được
            $.getJSON("https://provinces.open-api.vn/api/d/" + maQuanHuyen + "?depth=2", function(data) {
                // tìm và lấy mã code của phường/xã
                $.each(data.wards, function(index, value) {
                    if (value.name === phuongxa) {
                        maPhuongXa = value.code;
                        $('#PhuongXa').val(maPhuongXa).change();
                        return false;
                    }
                });

                // nếu không tìm thấy phường/xã thì trả về null
                if (!maPhuongXa) {
                    console.log("Không tìm thấy mã code cho phường/xã " + phuongxa);
                    return null;
                }
            });
        });
    });
};

$(document).ready(function() {
// Gọi API và lấy danh sách tỉnh/thành phố
    $.getJSON("https://provinces.open-api.vn/api/?depth=3", function(data) {
        var html = "";
        $.each(data, function(key, val) {
        html += "<option value='" + val.code + "'>" + val.name + "</option>";
        });
        $('#TinhThanh').html(html);
    });
    
    // Sự kiện khi chọn tỉnh thành phố
    $('#TinhThanh').on('change', function() {
        var codeTinhThanh = $(this).val();
        // Gọi lại API và lấy danh sách quận/huyện tương ứng với tỉnh/thành phố đã chọn
        $.getJSON("https://provinces.open-api.vn/api/p/" + codeTinhThanh + "?depth=2", function(data) {
        var html = "";
        $.each(data.districts, function(key, val) {
            html += "<option value='" + val.code + "'>" + val.name + "</option>";
        });
        $('#QuanHuyen').html(html);
        $('#PhuongXa').html("<option value=''>-- Chọn phường/xã --</option>");
        });
    });
    
    // Sự kiện khi chọn quận huyện
    $('#QuanHuyen').on('change', function() {
        var codeQuanHuyen = $(this).val();
        // Gọi lại API và lấy danh sách phường/xã tương ứng với quận/huyện đã chọn
        $.getJSON("https://provinces.open-api.vn/api/d/" + codeQuanHuyen + "?depth=2", function(data) {
        var html = "";
        $.each(data.wards, function(key, val) {
            html += "<option value='" + val.code + "'>" + val.name + "</option>";
        });
        $('#PhuongXa').html(html);
        });
    });
});
$('#ModalEDIT').on('show.bs.modal', function(event){
    var button = $(event.relatedTarget);
    // console.log(button);
    // lấy các giá trị từ data-* attribute
    var mssv = button.data('mssv');
    var hodem = button.data('hodem');
    var ten = button.data('ten');
    var lop = button.data('lop');
    var gioitinh = button.data('gioitinh');
    var dantoc = button.data('dantoc');
    var email = button.data('email');
    var sodt = button.data('sdt');
    var ngaysinh = button.data('ngaysinh');
    var noisinh = button.data('noisinh');
    var gioitinh_1_0= gioitinh.trim() == "Nam" ? 1 : 0;

    var parsedDate = new Date(ngaysinh);
    var day = parsedDate.getDate();
    var month = parsedDate.getMonth() + 1; // Cộng thêm 1 vì tháng trong JavaScript bắt đầu từ 0
    var year = parsedDate.getFullYear();

    var monthString = month < 10 ? "0"+month : month;
    var dayString = day < 10 ? "0"+day : day;
    // Tạo chuỗi mới theo định dạng mm/dd/yyyy
    var formattedDate = year + "-" + monthString + "-" +  dayString;
    //console.log(formattedDate);
    var tmp= noisinh.trim().split(",");
    // console.log(tmp);
    if (tmp.length == 5)
    {
        var TinhThanh= tmp[4].trim();
        var QuanHuyen= tmp[3].trim();
        var PhuongXa= tmp[2].trim();
        var sonhatenduong= tmp[0].trim() + "," + tmp[1].trim();
        // console.log("TRue")
    }
    else
    {
        var TinhThanh= "Thành phố Hồ Chí Minh";
        var QuanHuyen= tmp[2].trim();
        var PhuongXa= "Phường 2";
        var sonhatenduong= tmp[0].trim() + "," + tmp[1].trim();
    }
    // console.log(TinhThanh, QuanHuyen, PhuongXa, sonhatenduong);
    getCodes(TinhThanh, QuanHuyen, PhuongXa);
    // Gán giá trị cho các phần tử trong modal
    var modal = $(this);
    var hoten= hodem.trim() + " " + ten.trim();
    modal.find('#mssvEdit').val(mssv);
    modal.find('#hoTenGhiChuEdit').val(hoten);
    modal.find('#LopEdit').val(lop.trim());
    modal.find('#GioiTinhEdit').val(gioitinh_1_0);
    modal.find('#DanTocEdit').val(dantoc.trim());
    modal.find('#EmailEdit').val(email.trim());
    modal.find('#SoDTEdit').val(sodt);
    modal.find('#NgaySinhEdit').val(formattedDate);
    modal.find('#NoiSinhEdit').val(noisinh.trim());
    modal.find('#SoNhaTenDuong').val(sonhatenduong);
})

function checkInfoEDIT()
{
    var hoten= $("#hoTenGhiChuEdit").val();
    var lop= $("#LopEdit").val();
    var gioitinh= $("#GioiTinhEdit").val();
    var dantoc= $("#DanTocEdit").val();
    var email= $("#EmailEdit").val();
    var sodt= $("#SoDTEdit").val();
    var ngaysinh= $("#NgaySinhEdit").val();
    var noisinh= $("#NoiSinhEdit").val();
    var sonhatenduong= $("#SoNhaTenDuong").val();
    var tinhthanh= $("#TinhThanh option:selected").html();
    var quanhuyen= $("#QuanHuyen option:selected").html();
    var phuongxa= $("#PhuongXa option:selected").html();
    if (hoten == "" || lop == "" || gioitinh == "" || dantoc == "" || email == "" || sodt == "" || ngaysinh == "" || noisinh == "" || sonhatenduong == "" || tinhthanh == "" || quanhuyen == "" || phuongxa == "")
    {
        alert("Vui lòng nhập đầy đủ thông tin");
        return false;
    }
    return true;
}

$("#editInFoStudent").click(
    function()
    {
        if (checkInfoEDIT())
        {
            $.ajax({
                url: "/edit-info-student/",
                type: "POST",
                data:{
                    'mssv': $("#mssvEdit").val(),
                    'hoten': $("#hoTenGhiChuEdit").val(),
                    'lop': $("#LopEdit").val(),
                    'gioitinh': $("#GioiTinhEdit").val(),
                    'dantoc': $("#DanTocEdit").val(),
                    'email': $("#EmailEdit").val(),
                    'sodt': $("#SoDTEdit").val(),
                    'ngaysinh': $("#NgaySinhEdit").val(),
                    'sonhatenduong': $("#SoNhaTenDuong").val(),
                    'tinhthanh': $("#TinhThanh option:selected").html(),
                    'quanhuyen': $("#QuanHuyen option:selected").html(),
                    'phuongxa': $("#PhuongXa option:selected").html(),
                    'csrfmiddlewaretoken': '{{csrf_token}}'
                },
                success: function(data){
                    alert("Cập nhập thông tin thành công");
                    location.reload();
                },
                error: function(){
                    alert("Cập nhập thông tin thất bại");
                }
            })
        }
    }
);