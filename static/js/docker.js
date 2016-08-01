$("document").ready(function(){
    $(".stop-container").each(function(){
        $(this).click(function(e){
            //e.preventDefault();
            var container_id = $(this).attr("id");
            $.ajax({
                url:"container/stop",
                type: "POST",
                data: {id:container_id}
            })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });

    });

    $(".start-container").each(function(){
        $(this).click(function(e){
            //e.preventDefault();
            var container_id = $(this).attr("id");
            $.ajax({
                url:"container/start",
                type: "POST",
                data: {id:container_id}
            })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });

    });

    $(".command-container").each(function(){
        $(this).click(function(e){
            e.preventDefault();
            var command = prompt("Type the command will run into the container");
            var container_id = $(this).attr("id");
            $.ajax({
                url:"container/command",
                type: "POST",
                data: {id:container_id,command:command}
            })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });

    });

    $(".remove-container").each(function(){
        $(this).click(function(e){
            var container_id = $(this).attr("id");
            $.ajax({
                url:"container/delete",
                type: "DELETE",
                data: {id:container_id}
            })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });

    });

});
